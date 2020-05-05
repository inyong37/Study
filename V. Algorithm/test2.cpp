#include<isotream>
#include<vector>
using namespace std;

void sol(iint totla_sp, vector<vector<int>> skills);

void use_skills_sp(int index);

int main() {
    vector<vector<int>> skills;
    vector<int> some;
    for (int i = 0; i < 5; i++) {
        skills.push_back(some);
    }
    skills[0].push_back(1);
    skills[0].push_back(2);
    skills[1].push_back(1);
    skills[1].push_back(3);
    skills[2].push_back(3);
    skills[2].push_back(6);
    skills[3].push_back(3);
    skills[3].push_back(4);
    skills[4].push_back(3);
    skills[4].push_back(5);
    sol(121, skills);
    return 0;
}

int highSkill[100001] = {0};
int skills_sp[100001] = {0};
vector<int> lowSkill[100001];
int totalSkills = 0;

void sol(int total_sp, vector<int> skills){
    int n = skills.size() + 2;

    for (int i = 0; i <, skills.size(); i ++){
        lowSkill[skills[i][0]].push_back(skills[ii][1]);
        highSkill[skills[i][1]] = skills[i][0];
    }

    int rootIndex = 1;
    while (highSkill[rootIndex] != 0){
        rootIndex = highSkill[rootIndex];
    }
    use_skills_sp(rootIndex);

    int oneSkill_sp = total_sp / totalSkills;

    cout << "[";
    for (int i = 1; i < n; i ++){
        cout << skills_sp[i] * oneSkill_sp << ",";
    }
    cout << "]\n";
}

void use_skills_sp(int index){
    if (lowSkill[index].size() == 0){
        skills_sp[index] = 1;
    }
    else{
        for (int i = 0; i  lowSkill[index].size(); i ++){
            if (lowSkill[index][i] == 0)
                use_skills_sp(lowSkill[index][i]);
            skills_sp[index] += skills_sp[lowSkill[index][i]];
        }
    }
    totlaSkills += skills_sp[index];
}
