# epidemic_intelligence_model
SEIR-based model for analyzing information and misinformation spread in social networks

1. Problem Definition/Motivation
In today's connected world, misinformation can transmit quickly, influencing public opinion, policy choices, and even health behaviors.I wanted to represent information and misinformation transmitted in social networks via the principles of disease epidemiology because I find it interesting how information acts like contagious diseases in today's world.
For my model, I used five compartments: Susceptible (S), Exposed (E), Infectious (I), Recovered (R), and Skeptical (K). I used these particular compartments because they identify the most important states that people might be in as they are exposed to information:
Susceptible individuals have not yet come across the information
Exposed individuals have viewed the information but not yet decided to pass it on
Infectious individuals are currently passing on the information
Recovered individuals have ceased to spread the information
Skeptical individuals are immune to the information because of previous beliefs or fact-checking
I prefer this model because:
It uses familiar epidemiological principles to a contemporary social issue
It adds cognitive aspects like belief and skepticism
It can be utilized to explain why misinformation occasionally spreads more quickly than truth
It offers insights into possible intervention strategies
This model can actually be very effective in explaining events such as vaccine hesitancy, political polarisation, and viral disinformation campaigns that we observe on a regular basis within society.

2. Model Formulation (Equations/Rules)
In order to carry out this simulation of information spreading, I utilized a modified SEIR (Susceptible-Exposed-Infectious-Recovered) model that incorporates a further compartment for Skeptical individuals. This mathematical model is used because it captures both the epidemiological dynamics and the cognitive processes of information spreading.
My model uses the following difference equations in order to update the population within each compartment at each time step:
S(t+1) = S(t) - β·S(t)·I(t)/N - γ·S(t)
E(t+1) = E(t) + β·S(t)·I(t)/N - δ·E(t)
I(t+1) = I(t) + δ·E(t) - ρ·I(t)
R(t+1) = R(t) + ρ·I(t)
K(t+1) = K(t) + γ·S(t)
Where:
S, E, I, R, and K are the number of people in each compartment
N is the population size (S + E + I + R + K = 10,000 in my version)
β = 0.5 is the transmission rate (how well information propagates)
γ = 0.02 is the rate of skepticism among susceptible individuals
δ = 0.2 is the rate at which exposed become infectious (choose to share)
ρ = 0.05 is the rate at which infectious individuals choose not to share (recover)
These are equations for the following processes:
Susceptible individuals may become exposed to information by coming into contact with infectious individuals (at rate β) or skeptical (at rate γ)
Exposed individuals become infectious at rate δ once they make the decision to share
Infectious people eventually cease sharing and become recovered at rate ρ
Skeptical people stay skeptical during the simulation
The population N is kept constant at 10,000
I used these particular parameter values because they represent a moderately transmissible bit of information with sensible rates of skepticism and sharing decisions. The rate of transmission β = 0.5 implies that every infectious individual has a 50% probability of infecting susceptible individuals they interact with. The rate of skepticism γ = 0.02 implies that 2% of the susceptible individuals become skeptical every day without exposure to the information. The decision to share the information rate δ = 0.2 implies that 20% of exposed individuals make the decision to share the information every day. The rate of recovery ρ = 0.05 means that 5% of the infectious people cease sharing daily.


3. Implementation of the Model
To deploy my information diffusion model, I wrote a Python program that:
Declares the five compartments: Susceptible (S), Exposed (E), Infectious (I), Recovered (R), and Skeptical (K)
Initializes parameters β = 0.5 (transmission rate), γ = 0.02 (skepticism rate), δ = 0.2 (decision to share rate), and ρ = 0.05 (recovery rate)
Establishes the population size as N = 10,000 people
Initial conditions: 9,900 susceptible, 50 exposed, 30 infectious, 0 recovered, and 20 skeptical individuals
Simulates information spread for 60 days
Monitors and stores the number of people in each compartment at each time step
Plots the results with matplotlib
The heart of my program employs a loop to calculate the compartments at each time step based on the difference equations I established. At each day of my simulation, I:
Calculate new individuals exposed due to transmission (β·S·I/N)
Calculate new individuals becoming dubious (γ·S)
Calculate new individuals becoming infectious upon exposure (δ·E)
Calculate new individuals getting cured from sharing (ρ·I)
Update all compartments for the subsequent time step
Save the results for future analysis and visualization
Having done the simulation for 60 days, I create a plot of how the various compartments vary with time so that I can see trends in information dissemination and the efficiency of skepticism in blocking misinformation.

4. Exploration of the Model
I ran my information spread model with the particular parameters I used, and noticed a number of intriguing patterns throughout the course of the 60-day simulation.
4.1 General Dynamics
With my parameter values (β = 0.5, γ = 0.02, δ = 0.2, ρ = 0.05), I noticed the following dynamics:
The susceptible population decreased more rapidly over time, with around 500 people remaining susceptible by day 60
 The infectious population showed a more pronounced peak around day 15, reaching higher values before declining
 The exposed population reached a visible peak around day 10 before declining
 The recovered population climbed more steeply as infectious individuals ceased to share
The skeptical population increased linearly but more slowly with a rate based on γ, up to about 1,200 members on day 60
The simulation clearly illustrates the wave-like behavior characteristic of epidemic models, with more prominent peaks in the infectious and exposed populations.

4.2 Effect of Initial Conditions
I began with 9,900 susceptible, 50 exposed, 30 infectious, and 20 skeptical agents. These conditions reflect a starting point in which information has begun to spread through a large group of people. With the higher transmission rate, even the initially small infectious population (30) was enough to cause rapid and widespread diffusion throughout the population.
If I'd begun with fewer infectives (e.g., 5-10), then the spread would have been slightly more gradual at the start but would quickly accelerate to similar levels. Starting with more infectives, on the other hand, would have pushed early spread and resulted in an even faster initial propagation.
4.3 Sensitivity of parameters
While I didn't have parameter variation set up explicitly within my implementation, what I think about the model indicates:
Transmissibility (β = 0.5):
This higher value is for information that propagates very well, almost virally
If set higher to 0.7 or above, we would have even quicker spread and higher peak infectious counts
If set lower to 0.3 or below, the information may spread more slowly with lower peak infectious counts

Skepticism rate (γ = 0.02):
This value signifies 2% of susceptible people become skeptical per day
This produces a slower flow into the skeptical compartment, which allows more information spread
 If this value is smaller, even more individuals get exposed before becoming skeptical
If greater, information spread would be contained more effectively

Sharing decision rate (δ = 0.2):
This implies 20% of exposed people choose to share the information every day
This higher value reduces the lag between exposure and sharing
If higher, exposed persons would become infectious even sooner, further increasing spread
If lower, exposed persons would take longer to disseminate the information

Recovery rate (ρ = 0.05):
That is, 5% of infectious persons cease disseminating per day
 This yields an average dissemination period of approximately 20 days
If this were greater, individuals would disseminate for shorter intervals, lowering spread
 If smaller, extended dissemination would increase overall diffusion of the information

4.4 Graph Analysis
The Epidemic Intelligence Model graph demonstrates the way in which the information gets passed after 60 days. The Susceptible (blue line) in the beginning is nearly 10,000 but decreases as the people start to get the information. The Skeptical (black line) increases steadily up to a very small figure slightly above 1,200 at day 60, which signifies more and more people start questioning the information as time goes by.
The Infectious group (red line), the people who are actually spreading the information, is a bell-shaped curve. It peaks between day 20 and 25 with about 2,600 people, then it starts to decrease. The Exposed group (yellow line) is a smaller but similar curve that peaks earlier at day 10 to 15.
The Recovered group (green line), consisting of individuals who cease propagating the information, increases continuously and levels at around 4,300 by the end. This indicates increasing numbers of people cease sharing the information over time, particularly following the peak.


5. Conclusions
The following are some things that I have learned from studying the Epidemic Intelligence Model:

Effectiveness in Solving the Problem

My extended SEIR model with a skepticism compartment effectively mimics how news is spread along social networks. Using a 10,000 person population with realistic parameters, the model adequately models important dynamics such as:

The initial epidemic-like spread of new information
The peak and decline in share behavior
The preventive effect of skepticism in preventing spread
The subsequent stabilization of the system as news propagated runs its course

Such dynamics are reminiscent of what occurs in real information cascades in social media and imply that the epidemiological paradigm can be aptly applied in understanding information diffusion.

Personal Insights

Using this model has caused me to come closer to learning about both information dynamics and epidemiology. I've learned that:

Information dissemination follows predictable tendencies like disease propagation
Even a low rate of skepticism (5% per day) can lower total reach of information considerably
There seems to be some latency in the transition between seeing information and sharing it
Most information tends to have an organic life cycle with crest followed by decline

The biggest surprise was to observe how the exposed population acts as a reservoir feeding the infectious population, leading to a sustained but delayed mode of information transmission.

Limitations
This model has a few major limitations:

Network structure: My model applies homogeneous mixing (everyone has the same chance of contact), whereas actual social networks contain complicated structures with hubs and clusters
Individual differences: Humans have varying levels of vulnerability to information in terms of prior beliefs, not reflected in my model
Content evolution: Typically, information transforms when it travels, but according to my model, it's static
Time-varying parameters: Actually, transmission rates could vary because information becomes progressively less new over time
External influences: My model doesn't reflect media publicity or platform algorithmic amplifications that could cause certain information

Simple vs. Complex Models
While this model is simple in comparison to current information diffusion models, it has useful insights with the added benefits of being computationally tractable and interpretable. The five-compartment model (S-E-I-R-K) is well-balanced in terms of being able to capture important dynamics while still being simple.

From my perspective, this model can be expanded/enhanced by:

Adding different susceptibility based on person-specific traits
Including content-based parameters that incorporate emotional appeal or plausibility
Adding external interventions such as attempts at fact-checking

Overall, I found this investigation of the Epidemic Intelligence Model to be gratifying. Despite having a relatively simple five-compartment model and 60-day time frame for simulation, I managed to learn something about the subtle dynamics of information spread and determinants. Such a process could be beneficial in learning about and possibly forestalling harmful misinformation campaigns in the future.


