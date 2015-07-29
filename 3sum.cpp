typedef vector<int> vi;
vector<vector<int> > threeSum(vector<int> &num) {
    sort(num.begin(),num.end());
    vector<vi> result;
    int size = num.size();
    vi path;
    for(int i=0;i<size;i++){
        int a = i+1;
        int b = size-1;
        while(a<b){
            int tmp = num[a]+num[b]+num[i];
            if(tmp == 0){
                path.push_back(num[i]);
                path.push_back(num[a]);
                path.push_back(num[b]);
                result.push_back(path);
               
                a++;
                b--;
                while(a<b && path[1] == num[a]) a++;
                while(a<b && path[2] == num[b]) b--; 
                path.clear();
            }
            else{
                if(tmp<0) a++;
                else b--;
            }
        }
        while (i + 1 < num.size() && num[i + 1] == num[i]) i++;
    }
    return result;
}