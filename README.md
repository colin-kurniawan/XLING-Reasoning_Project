# XLING Reasoning Translation Exercise

## Project Overview
This repository is my attempt for the XLING-Reasoning Project Exercise. Under the result sections is where you can find my results along with the number of empty translations found in the dataset.

---

## Results

**Total Empty Translations Found:** *594*

### Language Pair: es-en

| Model | Best Method |
|-------|------------|
| deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B | teacher-CoT-translation |
| deepseek-ai/DeepSeek-R1-Distill-Llama-8B | teacher-CoT-translation |
| deepseek-ai/DeepSeek-R1-Distill-Qwen-7B | teacher-CoT-translation |
| Qwen/Qwen3-8B | teacher-CoT-translation |

### Language Pair: en-es

| Model | Best Method |
|-------|------------|
| deepseek-ai/DeepSeek-R1-Distill-Llama-8B | teacher-CoT-translation |
| Qwen/Qwen3-8B | teacher-CoT-translation |
| deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B | teacher-CoT-translation |
| deepseek-ai/DeepSeek-R1-Distill-Qwen-7B | self-CoT-translation |

### Language Pair: fr-en

| Model | Best Method |
|-------|------------|
| deepseek-ai/DeepSeek-R1-Distill-Llama-8B | self-CoT-translation |
| Qwen/Qwen3-8B | direct_translation |
| deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B | teacher-CoT-translation |
| deepseek-ai/DeepSeek-R1-Distill-Qwen-7B | teacher-CoT-translation |

---

## Conclusion
- The `teacher-CoT-translation` method frequently yields the highest BLEU scores most of the time. 

---
