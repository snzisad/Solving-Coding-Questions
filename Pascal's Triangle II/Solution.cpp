class Solution {
public:
    vector<int> getRow(int rowIndex) {
        rowIndex += 1;
        vector<int> rows = {};
        vector<int> row = {};
        
        for(int i=0; i<rowIndex; i++){
            rows.push_back(1);
            row = rows;
            for(int j=1; j<i; j++){
                rows[j] = row[j-1]+row[j];
            }
        }

        return rows;
    }
};