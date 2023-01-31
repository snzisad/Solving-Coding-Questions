class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> rows = {};
        vector<int> row = {};
        for(int i=1; i<=numRows; i++){
            row.clear();
            for(int j=0; j<i; j++){
                row.push_back(1);
            }
            rows.push_back(row);
        }

        for(int i=2; i<numRows; i++){
            for(int j=1; j<i; j++){
                rows[i][j] = rows[i-1][j-1]+rows[i-1][j];
            }
        }

        return rows;

    }
};