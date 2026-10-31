# Supervisor Meeting Transcript & Synthesis: Damian

**Date:** Friday, 23 October 2026, 14:42 CEST  
**Location:** TU Delft (Chemical Engineering / Catalysis Engineering)  
**Attendees:** Damian (Supervisor), Student (Author)  
**Context:** Bachelor End Project (BEP) in Catalysis / Reactor Modeling  

---

## 1. Executive Summary & Core Guidance

1. **Stop Meta-Planning & Tool Overload:**
   - Immediately abandon frontends, complex YAML map visualizers, and heavy planning tools.
   - Deliver clean, organized, directly runnable files: Jupyter Notebooks (`.ipynb`) and a clear `README.md` that Damian can open and run directly on his own computer.

2. **The Scientific Roadmap (Two-Step Modeling):**
   - **Step 1 (Grounding & Benchmark):** Select a published paper with experimental/industrial kinetic modeling data for acetylene semi-hydrogenation ($C_2H_2 + H_2 \rightarrow C_2H_4 \rightarrow C_2H_6$). Replicate their steady-state reactor model and prove that your code reproduces their exact published conversion/selectivity curves.
   - **Step 2 (The Novel Core - Dynamic / Periodic Operation):** Introduce transient dynamics and periodic operation.

3. **The Core Thesis Topic — CO Surface Modulation:**
   - **Why Hydrogen modulation is insufficient:** Modulating $H_2$ alone will not surpass steady-state performance due to reaction kinetics.
   - **The Role of CO (Carbon Monoxide):** 
     - Industrially present in acetylene tail-gas streams.
     - CO does not react with $H_2$ under these conditions; it acts as a reversible surface modifier / site-blocker (competitive adsorption / selective poisoning).
     - CO increases selectivity to ethylene ($C_2H_4$) by suppressing over-hydrogenation to ethane ($C_2H_6$), but simultaneously reduces overall activity (conversion).
     - **Thesis core hypothesis:** Dynamically tuning the surface coverage of CO via periodic inlet modulation can decouple the activity-selectivity trade-off and beat steady-state operation.

4. **Deliverables & Milestones:**
   - **Immediate / Monday:** Deliver clean, organized Jupyter notebook(s) + README with existing progress that Damian can open and inspect.
   - **End of Next Week:** Have a working, validated steady-state 1D reactor model reproducing a selected literature paper with kinetic parameters.
   - **Subsequent Phase:** Implement dynamic/transient reactor balances with periodic CO forcing.

---

## 2. Complete Meeting Transcript

> *Note: Transcribed from audio recording via `gemini-3.5-transcribe`.*

**Damian:** So just solve reactor balance. It is at hold up. In which repository is that one?

**Student:** So this was one of the first models and then let me see. Yes, this was just the test of the model and the actual plots are in...

**Damian:** Sure, but you know, it's okay, but feedback—it would be to organize yourself. Definitely. And I mean you should know what you've worked on. It should definitely be done by now. My advice is you have to learn, right? So don't use so much [AI tools]—it's going to kill your learning.

**Student:** So I have already reclaimed a lot of the info and I could show that if it just wants to load the frontend of that thing. 10 seconds, I look for the specific thing, I tell it to load the one from the latest PR as a backend map. And then hopefully that will...

**Damian:** Which version do you—

**Student:** I decided to get Plus because it's very useful.

**Damian:** Which one is the Plus?

**Student:** The 20 bucks.

**Damian:** Sure, anyways. So plan: you have a lot of—there exist a lot of papers that will use, that have kinetic parameters. You can just take theirs, it's not a problem. There are countless papers, just for now it's okay. I mean, I don't know if by the end of your thesis we will get to use this data because, yeah...

**Student:** There you go, now the notebook loaded. I'm listening.

**Damian:** So you can take kinetic parameters from the literature and implement the steady-state model, check that you get the same results as them, right? And then you can start implementing transient. That's very important. You will have all the equations, right? So then you can start trying to explain what your part of the thesis is, which is more the mathematics of periodic operation or whatever, not what the other paper did, because that's not what we're going to do.

Mostly related on CO, which is always present in—essentially carbon monoxide, so it's always present in this type of stream. So by tuning the concentration of CO on the surface you might be able to tune—it's much better than the hydrogen, because the hydrogen, you will never surpass steady state. Just the kinetics don't allow you to. Still interesting, but whatever.

**Student:** Okay, because... okay, so basically you have those streams, but there's also a stream for CO which is basically—I feel like something, oh, will CO react with H2?

**Damian:** No. So CO at these conditions will not react. So it's essentially CO leaving the catalyst, and CO on the catalyst will change how the catalyst works. So basically it's a replacement for inert gas because it interacts with the catalyst. It's always present industrially because you cannot remove it, but it's good for the catalyst because it makes it very selective. Right? So if it makes it more selective, what will happen to your conversion? Will it go high or low?

**Student:** More selective... well, selective towards a reactive reaction path. Ethylene, C2H4. If it makes it more selective towards that, that means—are we talking about adsorption? Okay, in that case it would prefer to react to ethylene compared to ethane, so yeah, then you would of course get more ethylene.

**Damian:** You would get more ethylene, yes, but that's very important: *selectively*. Selectivity is not to the conversion—that's sort of a trick question. But once you have high selectivity in this reaction, that typically is accompanied by low activity, meaning that you kill the catalyst; you make it more selective by killing the catalyst in a way or another. So the moment in which you have CO in there, your selectivity will be very high, but you can sort of tune the coverage of CO towards this effect.

**Student:** Poisoning and competitive adsorption.

**Damian:** Exactly. So please, there are many papers doing kinetic modeling of acetylene streams even with industrial reactor data, which is very interesting. So take those and just do steady-state reproduce, and this—you know, I trust that you know how to model—this should take you maybe one day.

**Student:** Especially with what I already have, if I can find it.

**Damian:** Anyways, please find it and just send me the Jupyter notebook files, or send me your repo or whatever, then I can check and then we can also check in my computer. So yeah, please. So I think now we're—I think what we've been trying has not been really working, so I think it's better.

**Student:** I definitely want to. First of all, this week I've had a lot more time for it, and in quarter two I also am taking on less other duties because I noticed it's, yeah...

**Damian:** That's okay, right? But you know, please by the end of this afternoon you tell me next week how much you can spend on this, and based on that I will give you a task. Right? Because if I—you know, typically what we try to do here is to let students sort of explore by themselves and guide, but that's not working. It's okay, there's no problem, but you know, sort of mark some deliverables that are needed, right? Because you need to be able to defend something, and right now you cannot defend if we project the progress over your end date. I mean, to be honest, I mean it's not enough for a BEP, right? So you know, we have to work towards that.

It's okay, you know, maybe we have to find—it very much depends person by person, so there's no problem. But you know, for next week, try to find one paper where they do kinetic modeling—there are millions, not millions, but maybe hundreds on acetylene semi-hydrogenation—and reproduce their results and send me the Jupyter notebook, and then we're going to discuss.

And by the way, it's very important to consider, right: you have to defend your thesis, so during your thesis you will not have access to [AI assistants]. It's okay if you want to use it, I don't care, but you have to understand that you have to learn. My advice is don't use it, right? Because the moment they catch you, right... it's very easy, very convenient once you already have the knowledge. Before that, you know, not only can it make mistakes, but also again it defeats the purpose of your thesis. I don't care how good your results are, I require that you learn, right? So if you don't learn anything, the committee, at least in this department, is not afraid of failing. And it's also my responsibility, right? Like I cannot give you a pass if you don't deserve a pass. Scientific integrity.

So we're going to do a system where every week you will have a deliverable that is just a Jupyter notebook file, it works fine, and then send it to me, I check it, and then we'll discuss and then proceed and move forward.

I also—being more organized, not only for yourself, but it's very important. I also, I have ADHD, right? So you probably also have it, maybe, I don't know.

**Student:** No clue.

**Damian:** Okay, but maybe, maybe you have it, I don't know. Anyways, it's okay, you know, it's the most important thing by far, right? And I'm not the most organized, so for people who are organized, much better, right? So it's your bachelor thesis, right? So it means after this you will have a degree from a very good university. So it means that you should be—like you should graduate being able to know where you keep a file, right? It's very important.

So just, you know, try to also spend some time in organizing your files. That's very important, especially in such computer simulation heavy work, right? I mean it's a must. Eventually when you're ready we are going to say fuck you to Jupyter notebooks because what the fuck are you doing there, right? So please really try to focus on being more organized, and we're going to switch to a model in which, you know, the deliverables with sort of pit stops to catch and check your understanding, right?

And also it's very important that you take it seriously, so you know, I'm trying to accommodate to you, so you know, you send me the files, etc., etc., but send them please, right? You know, it's hard for me, you know, to understand where you are if we cannot go through your results, right? So yeah, that's okay, it's no problem. I mean, you know, it's—yeah, that's a lot or whatever. It's okay, just send me all the details. That's why also, you know, I've been asking for weeks that you send me. It's okay, just do it.

**Student:** You see, it's still not—it's okay, keep thinking it's—well, one more day now, I think one more hour, but okay, at the end of the day we're definitely discussing again.

**Damian:** It needs something, right? It doesn't matter, I don't want frontend or whatever, fuck that. You send me the fucking TXT file, I don't care, but I'm going to freezing it too.

**Student:** Shit, I should have told you, motherfucker. You mean right now?

**Damian:** Right now.

**Student:** Motherfucker. But you come back on Sunday? You come back on Sunday? I'll text you. I'll be in, so I can go to you.

**Damian:** Anyways, yes, so you know, if a simple .txt...

**Student:** There should be here the file on GitHub, it's a YAML.

**Damian:** I here got to look at this right now, I mean basically, I mean this is not text, right? This is some HTML code, I mean I'm not going to sit down and...

**Student:** No, YAML is way more structured, this is the wrong one.

**Damian:** It's okay, but whatever, just send normal Word file, whatever, and then we can discuss, right? This is, you know, very important and I'm stressing it. I mean, you know, please. And if you have difficulties with the computer or whatever, I can try to arrange a computer for you, it's not a problem. I am willing to do this for you, but I need some reciprocation, right? I mean if I don't know that you're struggling because you don't have a computer, how can I expect, right? You know, you're shooting yourself in the foot. If you need a computer, I'll find you a computer. It's okay, right? Not a laptop, a computer, but I will find you one. I mean it's no problem.

But you know, it's important to discuss. You know, if you have a question, just text it to me. Don't ask, right? It's okay if you understand what you're working on, but I don't feel like you understand, so again you're shooting yourself in the foot, right? So it's okay, I understand it's a steep learning curve for you, you know, whatever, whatever. But please focus on the deliverables, right? And also, yeah, you know, you're a smart guy, so just, you know, you have to focus and complete the task. And then, you know, hopefully this system works. I hope, because it takes much more of my time, so please take it seriously because, yeah, it's very important. I mean, yeah, if not we cannot move forward.

So please, you know, by Monday send me all these Jupyter notebook files and a README file or whatever where I can see what you've been busy with—the actual thing, right?—that I can open in my own computer, okay? That will give you feedback. And then by the end of next week the goal would be to have a working model: steady-state with kinetic parameters from literature, okay? Very simple. I mean if you log in a couple of hours of code if you understand, right?

So please, okay, that's the deal that we have. Next week I'm in single drone again, but still send it to me, honestly. I can open Jupyter notebook files from there, right? So send it to me, and then we can discuss and proceed and move forward. Very important. And if you feel lost to whatever, just text me. I'm here to help you with that, right? Okay, you know, I don't know, let's say they have these equations, what does this term mean? You can ask, there's no problem, right? So please do that, okay? And then, yeah, please send this to me by Monday please. And yeah, and then the next thing would be on Friday after.

**Student:** Yes, so I think I have a very concrete direction right now. But for just so we are aligned again for this afternoon: the Jupyter notebook files of what you've been up to right now.

**Damian:** Yes, please, okay. I will even give you until Monday if you want.

**Student:** I'll round everything up to within—okay, now I don't give me a time because I mean, but if not today, that is a problem for me personally.

**Damian:** Oh okay, yeah, but then you have to do it today, so please do it.

**Student:** I want to deliver it right now.

**Damian:** Yes, good, see you. Which PR are we working on?
