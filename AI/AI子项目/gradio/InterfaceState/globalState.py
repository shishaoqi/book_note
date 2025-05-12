import gradio as gr

# 如果状态应该可供所有函数调用和所有用户访问，
# 则可以在函数调用外部创建一个变量并在函数内部访问它
scores = []

def track_score(score):
    scores.append(score)
    top_scores = sorted(scores, reverse=True)[:3]
    return top_scores

demo = gr.Interface(
    track_score, 
    gr.Number(label="Score"), 
    gr.JSON(label="Top Scores")
)
demo.launch()