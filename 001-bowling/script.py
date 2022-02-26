#!/usr/bin/env python3

"""A simple python script template.
"""

import argparse
import os
import sys

INPUT = 'X 45 4/ 32 X 45 4/ 32 11 1/ 3'
SCORES = [0] * 11


def _get_frames():
    # returns an array we can use to calculate
    # the scores for each frame
    return INPUT.split(' ')


def _get_frame_score(frame, frame_idx):

    is_strike = frame == 'X'
    is_spare = '/' in frame
    is_last_turn = frame_idx == 9
    is_bonus_turn = frame_idx == 10

    if (is_bonus_turn or is_last_turn) and (is_strike or is_spare):
        # strike or spare on bonus go or last go: return 10
        # the bonus frame score does not add to the last strike or spare
        return 10

    else:
        # here we know for sure we're not at the end
        # or we didn't run a strike/spare
        if is_strike:
            return 10 + SCORES[frame_idx + 1]
        elif is_spare:
            # pins cleared
            # get the first score of the next frame up, sum
            next_frame = _get_frames()[frame_idx + 1]
            return 10 + (10 if next_frame == 'X' else int(next_frame[0]))
        else:
            return sum([int(num) for num in frame])


def bowling():
    frames = _get_frames()

    for idx, frame in enumerate(frames[::-1]):
        # get the last frame's score
        # also get the last frame's mirrored index
        reverse_idx = len(frames) - (idx + 1)
        SCORES[reverse_idx] = _get_frame_score(frame, reverse_idx)


def main(arguments):
    bowling()
    for i, score in enumerate(SCORES):
        if i == 10:
            if score != 0:
                print('Bonus frame score: {}'.format(score))
            else:
                print('No bonus')
        else:
            print('Frame {} score: {}'.format(i + 1, score))
    print('Final: {}'.format(sum(SCORES)))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
