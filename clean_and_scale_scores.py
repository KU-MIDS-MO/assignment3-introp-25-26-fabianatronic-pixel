import numpy as np

def clean_and_scale_scores(scores, min_score, max_score):
    cleaned = np.array(scores, dtype=float)
    if cleaned.ndim == 1:
        for i in range (cleaned.shape[0]):
            if cleaned[i]< min_score:
                cleaned[i]= min_score
            elif cleaned [i]> max_score:
                cleaned[i]= max_score
            cleaned[i]=(cleaned[i]-min_score)/(max_score-min_score)
    elif cleaned.ndim == 2:
        for i in range (cleaned.shape[0]):
            for j in range(cleaned.shape[1]):
                if cleaned[i,j]<min_score:
                    cleaned[i,j]= min_score
                elif cleaned[i,j]> max_score:
                    cleaned[i,j]= max_score
                cleaned[i,j]= (cleaned[i,j]-min_score)/(max_score-min_score)
    return cleaned
#%%
# clean_and_scale_scores(scores, min_score, max_score)
#  We have exam scores stored in a NumPy array (1D or 2D).
#   - First, replace all values smaler than min_score by min_score,
#     and all values larger than max_score by max_score.
#    
 #  - Then linearly scale all values to the range [0, 1] using:
 #      scaled = (value - min_score) / (max_score - min_score)
#   Return a new NumPy array of floats with the same shape as scores