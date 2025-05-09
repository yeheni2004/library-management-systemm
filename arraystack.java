/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Yeheni
 */
public class arraystack {
    public class IntStack {
    private int[] stack;
    private int top;
    private static final int CAPACITY = 10;

    public IntStack() {
        stack = new int[CAPACITY];
        top = -1;
    }

    public void push(int item) {
        if (top == stack.length - 1) {
            resize(2 * stack.length);
        }
        stack[++top] = item;
    }

    public int pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack underflow");
        }
        int item = stack[top];
        stack[top--] = 0;
        return item;
    }

    public int peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        return stack[top];
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public boolean isFull() {
        return top == CAPACITY - 1;
    }

    public int size() {
        return top + 1;
    }

    private void resize(int newCapacity) {
        int[] newStack = new int[newCapacity];
        System.arraycopy(stack, 0, newStack, 0, size());
        stack = newStack;
    }

    public void printStack() {
        System.out.print("Stack (top to bottom): ");
        for (int i = top; i >= 0; i--) {
            System.out.print(stack[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        IntStack stack;
        stack = new IntStack();

        stack.push(10);
        stack.push(20);
        stack.push(30);
        System.out.println("Is Full? " + stack.isFull());
        stack.printStack();

        System.out.println("Top: " + stack.peek());
        System.out.println("Popped: " + stack.pop());
        stack.printStack();

        System.out.println("Size: " + stack.size());
        System.out.println("Is Empty? " + stack.isEmpty());
    }
}
    
}
