public class MedianList {

    class Solution2 {
        public double findMedianSortedArrays(int[] nums1, int[] nums2) {

            int aLength = nums1.length;
            int bLength = nums2.length;
            int aIndex = 0;
            int bIndex = 0;
            int[] newArray = new int[10];

            if (aLength == 0) {
                return checkResultArray(nums2);
            }

            if (bLength == 0) {
                return checkResultArray(nums1);
            }

            while(aIndex < bLength && bIndex < bLength) {
                int aValue = nums1[aIndex];
                int bValue = nums2[bIndex];

                if (aValue < bValue && aIndex < bLength - 1) {
                    newArray[] =
                    aIndex++;
                }



            }


            return 0;
        }


        public double checkResultArray(int[] resultArr) {


            return 0;
        }
    }



    public static void main (String[] args) {


    }

}



