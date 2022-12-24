class Solution {
    public String addBinary(String num1, String num2) {
        String sums = "";
        int carry = 0;
        char[] a = num1.toCharArray();
        char[] b = num2.toCharArray();
        int i=a.length-1;
        int j=b.length-1;

        while(i>=0 && j>=0){
            int binary_sum_data[] = binary_sum(a[i]-'0', b[j]-'0', carry);
            sums = binary_sum_data[0]+sums;
            carry = binary_sum_data[1];
            i--;
            j--;
        }
        while(i>=0){
            int binary_sum_data[] = binary_sum(a[i]-'0', 0, carry);
            sums = binary_sum_data[0]+sums;
            carry = binary_sum_data[1];
            i--;
        }
        while(j>=0){
            int binary_sum_data[] = binary_sum(0, b[j]-'0', carry);
            sums = binary_sum_data[0]+sums;
            carry = binary_sum_data[1];
            j--;
        }
        if(carry>0){
            sums = carry+sums;
        }

        return sums;
    }

    public int[] binary_sum(int a, int b, int carry){
        int sum1 = (a+b+carry);
        if(sum1 <= 1){
            carry = 0;
        }
        else if(sum1 == 2){
            sum1 = 0;
            carry = 1;
        } 
        else if (sum1 == 3) {
            sum1 = 1;
            carry = 1;
        }

        return new int[]{sum1, carry};
    }

    public static void main(String args[]){
        System.out.println(new Solution().addBinary("1010", "1011"));
    }
}