# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue {
    
    public:
    MyQueue(){        
    }
    
    stack <int> s1;
    stack <int> s2;    
        
    /** Push element x to the back of queue. */
    void push(int x) {
        s1.push(x);        
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if(s2.empty()){
            while(!s1.empty()){           
                s2.push(s1.top());
                s1.pop();
            } 
        }
        int topp = s2.top();
        s2.pop();       
        return topp;        
    }
    
    /** Get the front element. */
    int peek() {
        if(s2.empty()){
            while(!s1.empty()){           
                s2.push(s1.top());
                s1.pop();
            } 
        }      
        return s2.top();        
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        if (s1.empty() && s2.empty()){
            return true;
        }
        else{
            return false;
        }
        
        
    }
};
