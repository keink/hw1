#include<bits/stdc++.h>

using namespace std;

//文字列を小文字化する
string str_lower(string str){
	string ret="";
	for(int i=0;i<str.size();i++){
		ret+=tolower(str[i]);
	}
	return ret;
}

int main() {

	pair<string,string> dict[100010];
	string str;

	ifstream ifs("dictionary.txt");
	int dsize = 0;
	while(ifs)
	{
		ifs >> str;
		str=str_lower(str);
		
		//secondに元の文字列
		dict[dsize].second = str;
		for(int i=0;i<str.size();i++){
			//quをqにおきかえる
			if (str[i]=='q') {
				str.erase(str.begin()+i+1);
			}
		}
		sort(str.begin(), str.end());
		
		//firstにソートした文字列
		dict[dsize].first = str;
		dsize++;
	}
	
	//辞書もソート
	sort(dict, dict + dsize);
	
	//入力
	string x;
	cin >> x;
	
	sort(x.begin(), x.end());
	
	int max = 0;
	string z;
	for (int i = 1; i < ((int)1 << 16); i++)
	{
		string y="";
		
		int score = 0;
		//二進法
		for (int j = 0; j < 16; j++)
		{
			int k = (i >> j) % 2;
			if (k == 1) {
				y += x[j];
				//点数計算
				if (x[j] == 'j' || x[j] == 'k' || x[j] == 'q' || x[j] == 'x' || x[j] == 'z') {
					score += 3;
				}
				else if (x[j] == 'c' || x[j] == 'f' || x[j] == 'h' || x[j] == 'l' || x[j] == 'm' || x[j] == 'p' || x[j] == 'v' || x[j] == 'w' || x[j] == 'y') {
					score += 2;
				}
				else score += 1;
			}
			
		}
		//点数が最大値より大きかったら検索
		if (score > max) {
			int low = 0, high = dsize - 1, ret = -1;
			while (low < high) {
				if (y == dict[(low + high) / 2].first) {
					ret = (low + high) / 2;
					break;
				}
				else if (y > dict[(low + high) / 2].first) {
					low = (low + high) / 2 + 1;
				}
				else high = (low + high) / 2;
			}
			if (ret != -1) {
				
				z = dict[ret].second;
				//最大値の更新
				max = score;
				
			}
		}
	}
	cout << z << endl;
	return 0;
}
