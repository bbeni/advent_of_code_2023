#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

class BeamPart {
    public:
    int x, y;
    int dx, dy;
    BeamPart(int x_, int y_, int dx_, int dy_): x(x_), y(y_), dx(dx_), dy(dy_) {}
    bool inBounds(int w, int h)
    {
        return x<w && y<h && x>=0 && y>=0;
    }
};

bool isin(BeamPart b, vector<BeamPart> &parts)
{
    for (auto &part : parts)
    {
        if (b.x == part.x && b.y == part.y) return true;
    }
    return false;
}

bool isindir(BeamPart b, vector<BeamPart> parts)
{
    // check also direction
    for (auto &part : parts)
    {
        if (b.x == part.x && b.y == part.y && b.dx == part.dx && b.dy == part.dy) return true;
    }
    return false;
}

void printenergized(vector<BeamPart> parts, int w, int h)
{
    for( int i = 0; i<h; i++)
    {
        for ( int j = 0; j< w; j++)
        {
            if (isin(BeamPart(j, i, 0, 0), parts))
            {
                cout << '#';
            } else {
                cout << '.';
            }
        }
        cout << endl;
    }

}


int find_n_energized(std::vector<std::string> grid, BeamPart start, int max_iter)
{
    int w = grid[0].length();
    int h = grid.size();

    std::vector<BeamPart> beam {start};
    std::vector<BeamPart> found {};
    std::vector<BeamPart> found_directional {};
    for(int round=0; round<max_iter; round++ ) {
        //cout << "round: " << round << endl;
        std::vector<BeamPart> newbeam {};
        for(auto& bpart: beam) {
            if (!bpart.inBounds(w, h)) continue;

            if (isindir(bpart, found_directional))
            {
                //cancel loops
                continue;
            }
            found_directional.push_back(bpart);

            if (!isin(bpart, found)){
                found.push_back(bpart);
            }
            if (bpart.dx != 0) {
                // right or left
                switch (grid[bpart.y][bpart.x])
                {
                case '|':
                    newbeam.push_back(BeamPart(bpart.x, bpart.y-1, 0, -1));
                    newbeam.push_back(BeamPart(bpart.x, bpart.y+1, 0, 1));
                    break;
                case '/':
                    newbeam.push_back(BeamPart(bpart.x, bpart.y-bpart.dx, 0, -bpart.dx));
                    break;
                case '\\':
                    newbeam.push_back(BeamPart(bpart.x, bpart.y+bpart.dx, 0, bpart.dx));
                    break;
                default:
                    newbeam.push_back(BeamPart(bpart.x+bpart.dx, bpart.y, bpart.dx, bpart.dy));
                    break;
                }
            } else {
                // up or down
                switch (grid[bpart.y][bpart.x])
                {
                case '-':
                    newbeam.push_back(BeamPart(bpart.x-1, bpart.y, -1, 0));
                    newbeam.push_back(BeamPart(bpart.x+1, bpart.y, 1, 0));
                    break;
                case '/':
                    newbeam.push_back(BeamPart(bpart.x-bpart.dy, bpart.y, -bpart.dy, 0));
                    break;
                case '\\':
                    newbeam.push_back(BeamPart(bpart.x+bpart.dy, bpart.y, bpart.dy,0));
                    break;
                default:
                    newbeam.push_back(BeamPart(bpart.x, bpart.y+bpart.dy, bpart.dx, bpart.dy));
                    break;
                }
            }
            
        }
        beam.clear();
        beam = newbeam;

    }
    //printenergized(found, w, h);

    return found.size();
}

void problem1()
{
    std::vector<string> grid = {};
    std::ifstream file ("../inputs/in16.txt");
    for (std::string line; std::getline(file, line);)
    {
        grid.push_back(line);
    }
    file.close();

    cout << find_n_energized(grid, BeamPart(0,0,1,0), 10000) << endl;
}

void problem2()
{
    std::vector<string> grid = {};
    std::ifstream file ("../inputs/in16.txt");
    for (std::string line; std::getline(file, line);)
    {
        grid.push_back(line);
    }
    file.close();
    int w = grid[0].length();
    int h = grid.size();

    int max = 0;
    for (int i=0; i<w; i++)
    {
        int x = find_n_energized(grid, BeamPart(i,0,0,1), 10000);
        if (x>max) {max = x;}
    }
    
    for (int i=0; i<w; i++)
    {
        int x = find_n_energized(grid, BeamPart(i,h-1,0,-1), 10000);
        if (x>max) {max = x;}
    }
    
    for (int i=0; i<h; i++)
    {
        int x = find_n_energized(grid, BeamPart(0,i,1,0), 10000);
        if (x>max) {max = x;}
    }
    
    for (int i=0; i<h; i++)
    {
        int x = find_n_energized(grid, BeamPart(w-1,i,-1,0), 10000);
        if (x>max) {max = x;}
    }


    cout << max << endl;
}

int main()
{
    cout << "Day 16 in C++" << endl;
    problem1();
    problem2();
    return 0;
}