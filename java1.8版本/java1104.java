package daily1104;

public class java1104 {
    public static void main(String[] args) {

        int[] height = {1, 8, 6, 2, 5, 4, 8, 3, 7};

        System.out.println("最多可以盛水数目为：" + java1104.maxArea(height));

    }


    public static int maxArea( int[] height) {

        int l = 0, r = height.length - 1;
        int ans = 0;
        int maxx = 0;
        while (l < r) {
            maxx = (r - l) * Math.min(height[l], height[r]);

            ans = Math.max(maxx, ans);

            if (height[l] <= height[r]) {
                l++;
            } else {
                r--;
            }
        }


        return ans;
    }
}
