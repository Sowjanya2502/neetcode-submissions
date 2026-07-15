class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for (int r=0; r<grid.length; r++){
            for (int c=0; c<grid[0].length; c++){
                if (grid[r][c]=='1') {
                        count += dfs(r,c,grid);
                }
            }
        }
        return count;
        
    }

    public int dfs(int r, int c, char[][] grid) {
        if (!isValid(r, c, grid) || grid[r][c] != '1') {
            return 0;
        }

        grid[r][c] = '0';

        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        for (int i = 0; i < dirs.length; i++) {
            int newr = r + dirs[i][0];
            int newc = c + dirs[i][1];
            if (isValid(r, c, grid) || grid[r][c] == '1') {
            dfs(newr, newc, grid);
        }
        }
        return 1;
    }

    public boolean isValid(int r, int c, char[][] grid) {
        return r >= 0 && r < grid.length && c >= 0 && c < grid[0].length;
    }

}
