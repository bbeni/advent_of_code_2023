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

bool is_pos_in(BeamPart b, vector<BeamPart> &parts) {
    // check only for position
    for (auto &part : parts) 
    {
        if (b.x == part.x && b.y == part.y) return true;
    }
    return false;
}

bool is_in(BeamPart b, vector<BeamPart> &parts) {
    // check also direction
    for (auto &part : parts) 
    {
        if (b.x == part.x && b.y == part.y && b.dx == part.dx && b.dy == part.dy) return true;
    }
    return false;
}

void print_energized(vector<BeamPart> &parts, int w, int h)
{
    for( int i = 0; i<h; i++) 
    {
        for ( int j = 0; j< w; j++) 
        {
            if (is_pos_in(BeamPart(j, i, 0, 0), parts)) 
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

    std::vector<BeamPart> beam_front {start};
    std::vector<BeamPart> found_energized {};
    std::vector<BeamPart> found_directional {};
    for(int round=0; round<max_iter; round++ ) 
    {
        //cout << "round: " << round << endl;
        std::vector<BeamPart> next_beam_front {};
        for(auto& beam_part: beam_front) 
        {

            if (!beam_part.inBounds(w, h)) 
            {
                continue;
            }

            if (is_in(beam_part, found_directional)) 
            {
                //cancel loops
                continue;
            }
            found_directional.push_back(beam_part);

            if (!is_pos_in(beam_part, found_energized)) 
            {
                found_energized.push_back(beam_part);
            }

            if (beam_part.dx != 0) 
            {
                // right or left
                switch (grid[beam_part.y][beam_part.x])
                {
                case '|':
                    next_beam_front.push_back(BeamPart(beam_part.x, beam_part.y-1, 0, -1));
                    next_beam_front.push_back(BeamPart(beam_part.x, beam_part.y+1, 0, 1));
                    break;
                case '/':
                    next_beam_front.push_back(BeamPart(beam_part.x, beam_part.y-beam_part.dx, 0, -beam_part.dx));
                    break;
                case '\\':
                    next_beam_front.push_back(BeamPart(beam_part.x, beam_part.y+beam_part.dx, 0, beam_part.dx));
                    break;
                default:
                    next_beam_front.push_back(BeamPart(beam_part.x+beam_part.dx, beam_part.y, beam_part.dx, beam_part.dy));
                    break;
                }
            } else {
                // up or down
                switch (grid[beam_part.y][beam_part.x])
                {
                case '-':
                    next_beam_front.push_back(BeamPart(beam_part.x-1, beam_part.y, -1, 0));
                    next_beam_front.push_back(BeamPart(beam_part.x+1, beam_part.y, 1, 0));
                    break;
                case '/':
                    next_beam_front.push_back(BeamPart(beam_part.x-beam_part.dy, beam_part.y, -beam_part.dy, 0));
                    break;
                case '\\':
                    next_beam_front.push_back(BeamPart(beam_part.x+beam_part.dy, beam_part.y, beam_part.dy,0));
                    break;
                default:
                    next_beam_front.push_back(BeamPart(beam_part.x, beam_part.y+beam_part.dy, beam_part.dx, beam_part.dy));
                    break;
                }
            }
            
        }
        beam_front.clear();
        beam_front = next_beam_front;

    }
    //print_energized(found, w, h);
    return found_energized.size();
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