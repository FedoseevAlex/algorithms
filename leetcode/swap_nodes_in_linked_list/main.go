package main

import "fmt"

/*
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
               a 9 8 7 6 5 4 3 2 1
               1 2 3 4 5 6 7 8 9 a
                       f l
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 10^5
0 <= Node.val <= 100
*/

type ListNode struct {
	Val  int
	Next *ListNode
}

func swapNodes(head *ListNode, k int) *ListNode {
	fromStart := head
	fromEnd := head

	for node := head; node != nil; node = node.Next {
		k--
		if k > 0 {
			fromStart = fromStart.Next
		}

		if k < 0 {
			fromEnd = fromEnd.Next
		}
	}

	fromStart.Val, fromEnd.Val = fromEnd.Val, fromStart.Val
	return head
}

func printLinkedList(head *ListNode) {
	for head != nil {
		fmt.Print(head.Val)
		if head.Next != nil {
			fmt.Print(" -> ")
		}
		head = head.Next
	}
	fmt.Print("\n")
}

func main() {
	var (
		listHead    *ListNode
		currentHead *ListNode
	)

	for i := 1; i <= 5; i++ {
		if currentHead == nil {
			currentHead = &ListNode{Val: i}
			continue
		}
		if listHead == nil {
			listHead = currentHead
		}
		newNode := &ListNode{Val: i}
		currentHead.Next = newNode
		currentHead = newNode
	}

	printLinkedList(listHead)
	newHead := swapNodes(listHead, 2)
	printLinkedList(newHead)
}
