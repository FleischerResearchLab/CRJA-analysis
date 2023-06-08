---
layout: page
title: Racial Disparities in Police Stops Related to Homelessness
description:  Provide initial insight into the racial disparities in the San Diego criminal justice system
img: assets/img/press_con.jpg
importance: 1
date: 2023-05-19 11:01:00 +0800
category: Research
---
## Introduction
California Governor Gavin Newsom signed several laws after taking office in 2019 to promote racial equality and justice, one among which is the California Racial Justice Act (AB 2542). The key point of the RJA is that it allows defendants to challenge their sentences or convictions by presenting statistical evidence showing that race was a significant factor in their case, potentially leading to a new trial, a reduction in sentence, or a reversal of conviction. The act also requires the state to collect and analyze data on the race and ethnicity of individuals involved in the criminal justice system to identify and address racial disparities, with the end goal of increasing fairness and equity within the system.
The goal of this research is to seek acceptable statistical methods for demonstrating racial disparities by starting with the homelessness group in San Diego. We argue that by intentionally targeting the homeless, law enforcement is intentionally targeting minorities, who are known to be overrepresented in the homeless population. RJA motions can get the demographics before the court and the public to help influence the policymakers to end the criminalization of homeless people.

## Data
The data used in this analysis comes from two sources:
<ul>
    <li>The Racial and Identity Profiling Act (RIPA) stops dataset provided by the San Diego Police Department
    </li>
    <li>PRA 22-4296_inewsource_SDPD. 
        <ul><li> The Public Records Act (PRA) allows access to public records unless exempt from disclosure by law.</li></ul>
    </li>
</ul>

The RIPA dataset includes information on 679,019 police stops in the city of San Diego between July 1, 2018 and March 31, 2023 and was pre-processed to remove any sensitive information and to ensure data quality. It contains information on the demographic characteristics of individuals who were stopped by police, as well as information on the reason for the stop, the outcome of the stop, and whether a search was conducted.

The PRA 22-4296_inewsource_SDPD dataset was requested by our team via the Public Records Act, which allows access to public records unless exempt from disclosure by law. It contains information on 18,783 police charges in the city of San Diego from between January 1, 2018 and August 12, 2022. It contains similar information on the demographic characteristics of individuals who were **charged** by the police, including their race, ethnicity, gender, age, and location of the charge.

We filtered stops that are likely to be unhoused individuals by using a keyword list and a set of the most common code violations listed in the "stop reason explanation" column of the RIPA data that could potentially be homelessness-related .

According to Defense Attorney Coleen Cusack, there are 4 primary penal codes that are frequently used by officer involved with homelessness:
<ul>
    <li>San Diego Municipal Code 86.0137(f) Vehicle Habitation,</li>
    <li>San Diego Municipal Code 54.0110 Encroachment,</li>
    <li>San Diego Municipal Code 63.0102(b)(12) Overnight Camping,</li>
    <li>Penal Code 647(e) Illegal Lodging.</li>
</ul>

We decided to focus our analysis on these penal codes and extract the stops and charges related to these penal codes from our sources. We found 70,184 cases that are potentially related to homelessness, involving 52,223 stops and 28,844 charges, which composes 10.34% of the entirety of the traffic stop data.

To investigate the effect of racial bias in these stops and charges, we then isolated by charge and conducted outcome tests between minority races (Black/African-American and Asian) and the majority race (White.) Note that we’ve largely remained consistent with the racial categorization used within the RIPA data, defining "white" as not inclusive of Hispanic or Latino individuals & defining Asian as including East Asian countries but excluding South Asians, Middle Eastern individuals, and Pacific Islanders.

## Outcome Tests

We examined whether or not there is a racial disparity in stops related to home- lessness by employing outcome tests that involved comparing the stop action rate of minority groups (for a particular reason) for police stops with that same statistic of the majority group, the White (not Hispanic or Latino) population.

Here’s a quick summary of our results:
<table>
<caption>Table 1: Comparison of Outcome Tests Conducted for Homeless Populations in San Diego Across Both Datasets</caption>
<tbody>
<tr class="odd">
<td style="text-align: left;" rowspan="2"><strong>Homeless-related Charges</strong></td>
<td style="text-align: center;" colspan="2"><strong>Black vs. White</strong></td>
<td style="text-align: center;" colspan="2"><strong>Asian vs White</strong></td>
</tr>
<tr class="even">
<td style="text-align: center;"><strong>Citations</strong></td>
<td style="text-align: center;"><strong>Arrests</strong></td>
<td style="text-align: center;"><strong>Citations</strong></td>
<td style="text-align: center;"><strong>Arrests</strong></td>
</tr>
<tr class="odd">
<td style="text-align: left;">Overall Homeless-related Stops</td>
<td style="text-align: center;">1.49x</td>
<td style="text-align: center;">1.36x</td>
<td style="text-align: center;">1.2x</td>
<td style="text-align: center;">1.61x</td>
</tr>
<tr class="even">
<td style="text-align: left;">Vehicle Habitation</td>
<td style="text-align: center;">0.83x</td>
<td style="text-align: center;">0.92x</td>
<td style="text-align: center;">2.41x</td>
<td style="text-align: center;">4.41x</td>
</tr>
<tr class="odd">
<td style="text-align: left;">Illegal Lodging</td>
<td style="text-align: center;">1.57x</td>
<td style="text-align: center;">1.16x</td>
<td style="text-align: center;">1.33x</td>
<td style="text-align: center;">1.19x</td>
</tr>
<tr class="even">
<td style="text-align: left;">Unauthorized Encroachments Prohibited</td>
<td style="text-align: center;">1.54x</td>
<td style="text-align: center;">1.83x</td>
<td style="text-align: center;">1.07x</td>
<td style="text-align: center;">1.34x</td>
</tr>
</tbody>
</table>

The above table compares the cited/arrested individual against the SD county homeless population demographics, i.e. against the total racial demo- graphic breakdown of unhoused people in SD county. Here ”Overall Homeless Related Stops” refers to a composite figure of all the SD RIPA police stops related to ”Encroachment,” ”Illegal Lodging,” ”Vehicle Habitation,” as well as homelessness-related keywords (such as tent, property, transient, bags, home- less, unhoused, etc.) grouped together.

As a guide to reading this table: the first row indicates that a Black homeless individual is approximately **1.49 times (or 49%) more likely to be cited**, and **1.36 times or 36% more likely to be arrested**, than a White homeless individual for a homeless-related police stop in San Diego County. Similarly, we can see that an Asian homeless individual is **1.2 (or 20%) times more likely to be cited** and **1.61 (or 61%) times more likely to be arrested** than a White homeless individual.

Our analysis provides initial insight into the racial disparities in the San Diego criminal justice system and shows that Black and Asian individuals are disproportionately represented in arrests and citations for homelessness-related offenses as well as in the use of force by law enforcement officers. This points to systemic racial bias and raises questions about the effectiveness of current policies and practices in addressing crime and promoting racial equity in San Diego.
