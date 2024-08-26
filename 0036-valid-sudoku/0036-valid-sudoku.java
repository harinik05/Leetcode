class Solution {
    public ArrayList<Set<Character>> rows = new ArrayList<>();
    public ArrayList<Set<Character>> cols = new ArrayList<>();
    public ArrayList<Set<Character>> boxes = new ArrayList<>();


    
    public Solution() {
        // Initialize the ArrayLists with 9 empty sets
        for (int i = 0; i < 9; i++) {
            rows.add(new HashSet<>());
            cols.add(new HashSet<>());
            boxes.add(new HashSet<>());
        }
    }
    public boolean isValidSudoku(char[][] board) {
        //1. For loop 
        for(int i = 0;i<9;i++){
            for(int j = 0;j<9;j++){
                if(board[i][j] == '.'){
                    continue;
                }
                
                //check if its in rows 
                if(rows.get(i).contains(board[i][j])){
                    return false;
                }
                rows.get(i).add(board[i][j]);
                
                //check if its in cols 
                if(cols.get(j).contains(board[i][j])){
                    return false;
                }
                cols.get(j).add(board[i][j]);
                
                //check if its in boxes
                if(boxes.get((int)(i/3)*3 + (int)(j/3)).contains(board[i][j])){
                    return false;
                }
                boxes.get((int)(i/3)*3 + (int)(j/3)).add(board[i][j]);
                
                
                
                
            }
        }
        return true;
    }
}