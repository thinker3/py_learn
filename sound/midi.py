#!/usr/bin/env python
# -*- coding: utf-8 -*-


def pitch_to_frequency(p):
    f = 440 * 2 ** ((p - 69) / 12)
    return round(f, 3)


def get_dicts():
    note_pitch_dict = {}
    pitch_note_dict = {}
    pitch_frequency_dict = {}

    starters = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    for pitch in range(0, 128):
        quotient = (pitch // 12)
        remainder = pitch - 12 * quotient
        starter = starters[remainder]
        index = quotient - 1
        note = f'{starter}{index}'
        pitch_note_dict[pitch] = note
        note_pitch_dict[note] = pitch
        frequency = pitch_to_frequency(pitch)
        pitch_frequency_dict[pitch] = frequency

    print(note_pitch_dict)
    print()
    print(pitch_note_dict)
    print()
    print(pitch_frequency_dict)


def round3(x):
    return round(x, 3)


def get_octaves():
    starters = ['C', 'D', 'E', 'F', 'G', 'A', 'B', '2C']
    octaves = [1, 9/8, 81/64, 4/3, 3/2, 27/16, 243/128, 2]
    octaves = map(round3, octaves)
    octave_dict = dict(zip(starters, octaves))
    print(octave_dict)
    starters = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', '2C']
    v = 2 ** (1/12)
    twelves = []
    for i in range(13):
        twelves.append(v ** i)
    twelves = map(round3, twelves)
    twelve_dict = dict(zip(starters, twelves))
    print(twelve_dict)

get_octaves()
