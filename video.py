from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi


def summary(id):
    youtube_video = id
    video_id = youtube_video.split("=")[1]
    print(video_id)
    YouTubeTranscriptApi.get_transcript(video_id)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    result = ""
    for i in transcript:
        result += ' ' + i['text']
    summarizer = pipeline('summarization')
    num_inters = int(len(result) / 1000)
    summarized_text = []
    for i in range(0, num_inters + 1):
        start = 0
        start = i * 1000
        end = (i + 1) * 1000
        out = summarizer(result[start:end])
        out = out[0]
        out = out['summary_text']
        summarized_text.append(out)

    # print(str(summarized_text))
    summary_string = ' '.join([str(elem) for elem in summarized_text])
    return summary_string
