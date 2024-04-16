#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 生成一个100以内的随机数
int generateRandomNumber() {
    srand((unsigned)time(NULL));
    return rand() % 100 + 1;
}

// 进行猜数游戏
int guessNumber(int randomNumber, int maxGuess) {
    int guess, count = 0;

    // 循环进行猜数，直到猜中或超过最大次数
    while (1) {
        printf("Enter your guess: ");
        scanf("%d", &guess);
        count++;

        if (guess < 0) {
            printf("Game Over\n");
            return -1;
        } else if (guess == randomNumber) {
            printf("Bingo! You got it right in %d guesses.\n", count);
            return count;
        } else if (count >= maxGuess) {
            printf("Game Over. You have used all your guesses.\n");
            return -1;
        } else if (guess < randomNumber) {
            printf("Too small\n");
        } else {
            printf("Too big\n");
        }
    }
}

int main() {
    int randomNumber = generateRandomNumber();  // 生成随机数
    int maxGuess, result;

    printf("Enter the maximum number of guesses: ");
    scanf("%d", &maxGuess);  // 输入最大猜测次数
    
    result = guessNumber(randomNumber, maxGuess);  // 进行猜数游戏

    // 根据猜对的次数给出不同的提示
    if (result == 1) {
        printf("Bingo! You got it right in the first guess!\n");
    } else if (result > 1 && result <= 3) {
        printf("Lucky You! You got it right in %d guesses.\n", result);
    } else if (result > 3 && result != -1) {
        printf("Good Guess! You got it right in %d guesses.\n", result);
    }

    return 0;
}

