/**
 * @author vincent
 */
public class NoDuplicateString {
    int maxLength = 1;
    public int lengthOfLongestSubstring(String s) {
        //abcabcab
        if (s.length() >= 1) {
            checkDuplicate(0, 1, s);
        } else {
            maxLength = 0;
        }
        return maxLength;
    }

    public void checkDuplicate(int leftIndex, int rightIndex, String s) {
        String subString = s.substring(leftIndex, rightIndex);
        int subStringLength = subString.length();
        char checkChar = subString.charAt(subStringLength - 1);
        boolean isDuplicate = false;

        for(int i = 0; i < subString.length() - 1; i ++) {
            if (checkChar == subString.charAt(i)) {
                isDuplicate = true;
                break;
            }
        }

        if (isDuplicate) {
            // 右index 已经到达了最大的长度
            leftIndex ++;
        } else {
            maxLength = Math.max(subStringLength, maxLength);
            rightIndex ++;
        }

        if (rightIndex - 1 == s.length()) {
            return;
        }

        checkDuplicate(leftIndex, rightIndex, s);
    }

    public static void main(String[] args) {

        NoDuplicateString test = new NoDuplicateString();
        System.out.println(test.lengthOfLongestSubstring("au"));
    }


}
