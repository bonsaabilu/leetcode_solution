
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {

        ListNode* dummy = new ListNode(0);
        dummy->next = head;

        ListNode* prev = dummy;
        ListNode* curr = head;

        while (curr != nullptr) {

            // Check if current value has duplicates
            if (curr->next != nullptr &&
                curr->val == curr->next->val) {

                // Skip all nodes with the same value
                int duplicate = curr->val;

                while (curr != nullptr &&
                       curr->val == duplicate) {
                    curr = curr->next;
                }

                prev->next = curr;
            }
            else {
                prev = curr;
                curr = curr->next;
            }
        }

        return dummy->next;
    }
};
