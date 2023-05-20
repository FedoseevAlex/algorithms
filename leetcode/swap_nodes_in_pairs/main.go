package main

import "fmt"

/*
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Input: head = []
Output: []

Input: head = [1]
Output: [1]
*/

type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairsIterative(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	var (
		prev    *ListNode
		next    = head.Next
		newHead = head
	)
	if next != nil {
		newHead = next
	}
	for i := 0; next != nil; i++ {
		if i%2 == 0 {
			head.Next, next.Next = next.Next, head
			if prev != nil {
				prev.Next = next
			}
			head, next = next, head
		}
		prev, head, next = head, next, next.Next
	}
	return newHead
}

func swapPairsRecursive(head *ListNode) *ListNode {
	if head != nil && head.Next != nil {
		head, head.Next, head.Next.Next = head.Next, swapPairsRecursive(head.Next.Next), head
	}
	return head
}

func reverseLinkedList(head *ListNode) *ListNode {
	var (
		prev *ListNode
		next = head.Next
	)
	for head != nil {
		head.Next = prev
		if next == nil {
			break
		}
		prev, head, next = head, next, next.Next
	}
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

	for i := 0; i < 5; i++ {
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
	newHead := swapPairsRecursive(listHead)
	//newHead := swapPairsIterative(listHead)
	//newHead := reverseLinkedList(listHead)
	printLinkedList(newHead)
}
