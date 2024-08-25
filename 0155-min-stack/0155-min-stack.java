class MinStack {
    private Stack<int[]> stack = new Stack<>();
    public MinStack() {
        
        
    }
    
    public void push(int val) {
        if(this.stack.isEmpty()){
            this.stack.push(new int[]{val, val});
        }else{
            int currentMin = this.stack.peek()[1];
            this.stack.push(new int[]{val, Math.min(val,currentMin)});
        }
    }
    
    public void pop() {
        this.stack.pop();
        
    }
    
    public int top() {
        return this.stack.peek()[0];
    }
    
    public int getMin() {
        return this.stack.peek()[1];
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */