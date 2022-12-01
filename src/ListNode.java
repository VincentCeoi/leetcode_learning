
//给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
//
// 请你将两个数相加，并以相同形式返回一个表示和的链表。 
//
// 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。 
//
// 
//
// 示例 1： 
// 
// 
//输入：l1 = [2,4,3], l2 = [5,6,4]
//输出：[7,0,8]
//解释：342 + 465 = 807.
// 
//
// 示例 2： 
//
// 
//输入：l1 = [0], l2 = [0]
//输出：[0]
// 
//
// 示例 3： 
//
// 
//输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
//输出：[8,9,9,9,0,0,0,1]
// 
//
// 
//
// 提示： 
//
// 
// 每个链表中的节点数在范围 [1, 100] 内 
// 0 <= Node.val <= 9 
// 题目数据保证列表表示的数字不含前导零 
// 
//
// Related Topics 递归 链表 数学 👍 8896 👎 0


//leetcode submit region begin(Prohibit modification and deletion)

// Definition for singly-linked list.
public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        //result node
        ListNode currentNode = new ListNode();

        //each next node;
        ListNode headNode = currentNode;


        int l1value = 0;
        int l2Value = 0;
        int plusValue = 0;


        while(true) {
            //default 0 is null
            if (l1 != null) {
                l1value = l1.val;
            } else {
                l1value = 0;
                l1 = l1.next;
            }

            if (l2 != null)  {
                l2Value = l2.val;
            } else {
                l2Value = 0;
                l2 = l2.next;
            }
            //int currentValue =

            //计算相加之后的总数，如果总和大于10, plusValue （即进位） 需要加一
            int sum = l1value + l2Value + plusValue;
            currentNode.val = sum % 10;

            if (sum >= 10) {
                plusValue = 1;
            } else {
                plusValue = 0;
            }

            //当3 个值都为0 时， 即目前已经循环结束，不要
            if (plusValue == 0 && l1 == null && l2 == null) {
                break;
            }

            //currentNode.value = (l1value + l2Value + plusValue) % 10;

            //plusValue = (l1value + l2Value + plusValue) % 10;
            //currentNode.value =
            ListNode nextNode = new ListNode();
            currentNode.next = nextNode;
        }

        return headNode;
    }


    public static void main (String[] args) {
        ListNode l1 = new ListNode(1);
        ListNode l2 = new ListNode(2);
        ListNode l3 = new ListNode(3);
    }
}