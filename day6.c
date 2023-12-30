#include <stdio.h>

typedef struct {
    long long int time;
    long long int distance;
} Race;

long long int wayWin(long long int time, long long int dist) {
    long long int ways = 0;
    for (long long int hold_time = 0; hold_time < time; ++hold_time) {
        long long int mt = time - hold_time;
        long long total_distance = (long long)mt * hold_time;
        if (total_distance > dist) {
            ways++;
        }
    }
    return ways;
}

int main() {
    Race races[] = {
        {49, 298},
        {78, 1185},
        {79, 1066},
        {80, 1181}
    };
    long long int num_races = sizeof(races) / sizeof(races[0]);

    long long total = 1;
    for (long long int i = 0; i < num_races; ++i) {
        total *= wayWin(races[i].time, races[i].distance);
    }
    printf("Part 1: %lld\n", total);

    long long int single_time = 49787980;
    long long single_dist = 298118510661181LL;
    printf("Part 2: %lld\n", wayWin(single_time, single_dist));

    return 0;
}
