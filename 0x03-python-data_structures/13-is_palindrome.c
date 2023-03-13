#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list. */
struct ListNode {
    int val;
    struct ListNode *next;
};

typedef struct ListNode listint_t;

/* Reverse a linked list in-place */
listint_t* reverseList(listint_t* head) {
    listint_t *prev = NULL, *next = NULL;
    while (head != NULL) {
        next = head->next;
        head->next = prev;
        prev = head;
        head = next;
    }
    return prev;
}

/* Check if a linked list is a palindrome */
int is_palindrome(listint_t** head) {
    if (*head == NULL || (*head)->next == NULL) {
        /* An empty list or a list with only one node is considered a palindrome */
        return 1;
    }
    
    /* Use two pointers to find the middle of the linked list */
    listint_t *slow = *head, *fast = *head;
    while (fast->next != NULL && fast->next->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }
    
    /* Reverse the second half of the linked list */
    listint_t *head2 = reverseList(slow->next);
    
    /* Compare the first half and the second half of the linked list */
    listint_t *p1 = *head, *p2 = head2;
    while (p2 != NULL) {
        if (p1->val != p2->val) {
            /* Not a palindrome */
            return 0;
        }
        p1 = p1->next;
        p2 = p2->next;
    }
    
    /* Restore the original linked list */
    reverseList(head2);
    
    /* The linked list is a palindrome */
    return 1;
}

/* Helper function to create a linked list */
listint_t* createList(int arr[], int n) {
    listint_t dummy, *tail = &dummy;
    for (int i = 0; i < n; i++) {
        tail->next = malloc(sizeof(listint_t));
        tail = tail->next;
        tail->val = arr[i];
        tail->next = NULL;
    }
    return dummy.next;
}

/* Helper function to print a linked list */
void printList(listint_t* head) {
    while (head != NULL) {
        printf("%d ", head->val);
        head = head->next;
    }
    printf("\n");
}

/* Main function for testing */
int main() {
    int arr1[] = {1, 2, 3, 2, 1};
    listint_t *list1 = createList(arr1, 5);
    printf("list1: ");
    printList(list1);
    printf("is_palindrome(list1) = %d\n", is_palindrome(&list1));

    int arr2[] = {1, 2, 3, 3, 2, 1};
    listint_t *list2 = createList(arr2, 6);
    printf("list2: ");
    printList(list2);
    printf("is_palindrome(list2) = %d\n", is_palindrome(&list2));

    int arr3[] = {1, 2, 3, 4, 5};
    listint_t *list3 = createList(arr3, 5);
    printf("list3: ");
    printList(list3);
    printf("is_palindrome(list3) = %d\n

