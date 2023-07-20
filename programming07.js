function solution(number, k) {
    const stack = [];
    let count = 0;

    for (const elem of number) {
        while(count < k && stack[stack.length-1] < elem){
            stack.pop();
            count += 1;
        }
        stack.push(elem);
    }
    while (count < k) {
        stack.pop()
        count += 1;
    }
    return stack.join("")
}