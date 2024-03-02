// NOT WORKING

#include <iostream>
#include <string>
#include <cuda_runtime.h>

__global__ void countOccurrences(char* str, char* word, int* result, int length) {
    int tid = blockIdx.x * blockDim.x + threadIdx.x;
    int wordLength = strlen(word);

    if (tid < length) {
        if (tid + wordLength <= length) {
            bool match = true;
            for (int i = 0; i < wordLength; i++) {
                if (str[tid + i] != word[i]) {
                    match = false;
                    break;
                }
            }

            if (match) {
                atomicAdd(result, 1);
            }
        }
    }
}

int main() {
    std::string text = "Hello world, hello world!";
    std::string word = "world";
    int textLength = text.size();
    int wordLength = word.size();

    char* d_text;
    char* d_word;
    int* d_result;

    cudaMalloc((void**)&d_text, textLength * sizeof(char));
    cudaMalloc((void**)&d_word, wordLength * sizeof(char));
    cudaMalloc((void**)&d_result, sizeof(int));

    cudaMemcpy(d_text, text.c_str(), textLength * sizeof(char), cudaMemcpyHostToDevice);
    cudaMemcpy(d_word, word.c_str(), wordLength * sizeof(char), cudaMemcpyHostToDevice);
    cudaMemset(d_result, 0, sizeof(int));

    int block_size = 32;
    int num_blocks = (textLength + block_size - 1) / block_size;

    countOccurrences<<<num_blocks, block_size>>>(d_text, d_word, d_result, textLength);

    int result;
    cudaMemcpy(&result, d_result, sizeof(int), cudaMemcpyDeviceToHost);

    std::cout << "Occurrences of the word \"" << word << "\": " << result << std::endl;

    cudaFree(d_text);
    cudaFree(d_word);
    cudaFree(d_result);

    return 0;
}
