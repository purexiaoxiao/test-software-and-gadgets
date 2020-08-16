#include <bits/stdc++.h>
using namespace std;
struct node
{ /*总分,c语言成绩,python成绩,数学成绩,线性代数成绩,英语成绩,形势与政策成绩,概率与统计成绩,离散数学成绩*/
    string name;
    int sum, cScore, pythonScore, mathScore, linearScore, englishScore, situationAndPolicyScore, probabilityAndStatisticsScore, discreteMathematicsScore;
    node *pre, *next;
};
extern "C"
{
    void Alignment();
    void show();
    void createaList();
    void test(char *p);
    bool mycmp(node *a, node *b);
}
struct label
{
    string label1, label2, label3, label4, label5, label6, label7, label8, label9, label10;
};
label *first;
char path[1024];
int n = 0;
node *arr[10000];
void Alignment(); //将数组和链表对齐
void show();
void createaList();
void write();
node *root;
void sort();
bool mycmp(node *a, node *b);
int main()
{
    char s[] = "D:/xls/2.xls";
    test(s);
    return 0;
}
void test(char *p)
{
    strcpy(path, p);
    createaList();
    sort(arr + 0, arr + n, mycmp);
    Alignment();

    write();
}
bool mycmp(node *a, node *b)
{
    return a->sum > b->sum;
}
void show()
{
    node *temp = root->next;
    while (temp != NULL)
    {
        printf("%d ", temp->sum);
        temp = temp->next;
    }
}
void Alignment()
{

    root->next = arr[0];
    for (int i = 1; i < n; i++)
    {
        arr[i - 1]->next = arr[i];
        arr[i]->pre = arr[i - 1];
    }
    arr[n - 1]->next = NULL;
}

void createaList()
{
    root = new node;
    root->next = root->pre = NULL;
    ifstream file;
    file.open(path);

    node *temp = root;
    char alpha;
    first = new label;
    file >> first->label1 >> first->label2 >> first->label3 >> first->label4 >> first->label5 >> first->label6 >> first->label7 >> first->label8 >> first->label9 >> first->label10;
    while (1)
    {
        if (file.eof())
        {
            n--;
            break;
        }
        temp->next = new node;
        temp->next->pre = temp;
        temp->next->next = NULL;
        temp = temp->next;
        file >> temp->name >> temp->cScore >> temp->pythonScore >> temp->mathScore >> temp->discreteMathematicsScore >> temp->linearScore >> temp->englishScore >> temp->probabilityAndStatisticsScore >> temp->probabilityAndStatisticsScore >> temp->sum;
        arr[n] = temp;
        n++;
    }
}
void write()
{
    ofstream file;
    file.open(path);

    node *temp = root;
    file << first->label1 << "\t" << first->label2 << "\t" << first->label3 << "\t" << first->label4 << "\t" << first->label5 << "\t" << first->label6 << "\t" << first->label7 << "\t" << first->label8 << "\t" << first->label9 << "\t" << first->label10 << endl;
    for (int i = 0; i < n; i++)
    {

        temp = temp->next;
        file << temp->name << "\t" << temp->cScore << "\t" << temp->pythonScore << "\t" << temp->mathScore << "\t" << temp->discreteMathematicsScore << "\t" << temp->linearScore << "\t" << temp->englishScore << "\t" << temp->probabilityAndStatisticsScore << "\t" << temp->probabilityAndStatisticsScore << "\t" << temp->sum << endl;
    }
}