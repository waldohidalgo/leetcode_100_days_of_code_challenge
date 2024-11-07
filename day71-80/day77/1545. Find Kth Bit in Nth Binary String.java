class Solution {
    public char findKthBit(int n, int k) { 
        return findBit(n, k);
    }
    private char findBit(int n, int k) {
        if (n == 1) {
            return '0';
        } 
        int length = (1 << n) - 1; 
        if (k == (length / 2) + 1) {
            return '1';
        } 
        if (k < (length / 2) + 1) {
            return findBit(n - 1, k);
        } 
        return findBit(n - 1, length - k + 1) == '0' ? '1' : '0';
    }
}
