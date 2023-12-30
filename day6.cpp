#include<bits/stdc++.h>

class Race {
public:
    long long int time;
    long long int distance;

    Race(long long int t, long long int d) : time(t), distance(d) {}
};

long long int wayWin(long long int time, long long int dist) {
    long long int ways = 0;
    for (int hold_time = 0; hold_time < time; ++hold_time) {
        long long int mt = time - hold_time;
        long total_distance = mt * (long)hold_time;
        if (total_distance > dist) {
            ways++;
        }
    }
    return ways;
}

int main() {
    std::vector<Race> races = {
        Race(49, 298),
        Race(78, 1185),
        Race(79, 1066),
        Race(80, 1181)
    };

    long long int total = 1;
    for (Race& race : races) {
        total *= wayWin(race.time, race.distance);
    }
    std::cout << "Part 1: " << total << std::endl;

    long long int single_time = 49787980;
    long long single_dist = 298118510661181LL;
    std::cout << "Part 2: " << wayWin(single_time, single_dist) << std::endl;

    return 0;
}
