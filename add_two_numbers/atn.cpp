//
// Created by kolaq on 01.06.2021.
//

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    int sum = 0;
    ListNode *l3 = NULL;
    ListNode **node = &l3;

    while (l1 != NULL || l2 != NULL || sum > 0) {
        if (l1 != NULL) {
            sum += l1->val;
            l1 = l1->next;
        }

        if (l2 != NULL) {
            sum += l2->val;
            l2 = l2->next;
        }

//        setting sum in new node
        *node = new ListNode(sum % 10);

//        setting carry for next loop
        sum /= 10;

//        switching to next node
        node = &((*node)->next);
    }
    return l3;
}