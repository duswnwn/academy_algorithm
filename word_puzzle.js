function solution(strs, t) {
    const dp = Array.from({length: t.length +1}, () => 0); //t의 길이 +1 만큼 배열 선언
    const strsSet = new Set(strs); //문자열 리스트 set으로 만들어 줌

    for (let i = 1; i < t.length + 1; i++) {
        dp[i] = Infinity; //문자열의 최솟값 무한대로 초기설정

        for (let j = 1; j < Math.min(i + 1, 6); j++) {
            const start = i - j;
            const end = i;

            //단어 조각이 있을 경우
            if (strsSet.has(t.slice(start, end))) {
                dp[i] = Math.min(dp[i], dp[i - j] + 1);
            }
        }
    }
    return dp[dp.length - 1] === Infinity ? -1 : dp[dp.length - 1];
}