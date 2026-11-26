# NOTES — THE WORLD IN ONE DAY, Wednesday 25 November 2026 (v2, winner template)

A program-drawn broadsheet summing up Wednesday 25 November 2026 in one
image: **41 stories across 8 regions** — masthead + giant date + red
3-story lead line; a day-in-numbers strip; a region bar with counts; a UTC
timeline; 3 hero stories with flat illustrations; 10 more illustrated
stories; an "ALSO ON WEDNESDAY" briefs list with source codes; a dotted
world map with numbered pins; a DATE CHECK footer; a HOW SURE legend.

Every story below happened or was first reported on 25 November 2026
(UTC). Nothing is invented, hyped, or speculative: each line states what
was reported, claims are attributed, and the DATE CHECK names near-miss
stories from earlier days that were deliberately left out.

## Stories and sources

### The three big stories (heroes)
1. Ukraine confirms drone strike on Russian cargo ship in the Gulf of
   Finland — President Zelenskiy confirms responsibility; 16 crew
   evacuated, ship towed to St Petersburg; Norway urges caution.
   Source: Reuters. [CONFIRMED]
2. China launches Shenzhou-24: Pakistani astronaut Muhammad Zeeshan Ali,
   40, becomes the first Pakistani in orbit and the first foreign
   astronaut aboard Tiangong; crew Tang Hongbo and Wu Yi; launch 08:18
   Beijing time (00:18 UTC) from Jiuquan. Source: Reuters / AP. [OFFICIAL]
3. Houthis hit Riyadh's tallest tower, 11 wounded — second strike within
   days. Source: Reuters (Saudi Civil Defence). [REPORTED]

### Ten more stories (illustrated, 4–13)
4. China's Huawei convicted in sprawling US criminal trial over Iran
   business; guilty on trade secrets, acquitted of racketeering.
   Source: Reuters. [OFFICIAL]
5. Dow erases a 1,100-point intraday plunge to close at 50,182.95
   (+0.33%); Nasdaq falls 0.62% as Nvidia slides 3.9%.
   Source: Reuters. [CONFIRMED]
6. Dell reports doubled sales of $54.9bn and $60.2bn in new AI server
   orders; shares rise 4.1% after hours. Source: Reuters. [OFFICIAL]
7. Magnitude 5.6 earthquake strikes Nepal's Koshi province near the China
   border. Source: EMSC. [OFFICIAL]
8. French officials order ex-president Sarkozy's corruption case (with
   wife Carla Bruni) to trial; first hearing 1 April 2027.
   Source: Reuters. [OFFICIAL]
9. Israeli airstrikes kill Naim Abu Nahl, Hamas-run interior ministry
   security chief, west of Gaza City. Source: AP. [REPORTED]
10. Asian stocks tumble on fresh US tariff threats: Korea down 5.3%,
    Taiwan down 5.1%, Nikkei down 2.9%. Source: Reuters. [CONFIRMED]
11. Trump awards Rudy Giuliani the Presidential Medal of Freedom.
    Source: Reuters. [OFFICIAL]
12. Vaibhav Sooryavanshi, 15, smashes 204 off 53 balls for India A against
    UAE, a record double century. Source: press reports. [REPORTED]
13. Brazil zoo hails the birth of a Spix's macaw chick as a boost for the
    species' recovery. Source: Reuters. [REPORTED]

### Also on Wednesday (briefs, 14–41)
14. Russian strike on Zaporizhzhia kills 2, wounds 22 [Reuters]
15. Putin: Ukraine keeps hitting refineries despite Trump's requests [Reuters]
16. Latvian president Rinkevics sees a possible "tipping point" in the
    Ukraine war next year [Reuters]
17. Swedish PM Andersson fails again in her bid to form a government [Wire]
18. Norway urges Kyiv to exercise caution in such operations [Reuters]
19. NATO chief promises safeguarding against space threat after reports of
    Russian nuclear satellites [Wire]
20. Houthis push to within 60 km of Aden; Yemeni military says they will
    not seize the city [Reuters]
21. Houthis report 25 dead or missing in Saudi airstrikes in southern
    Yemen [Wire]
22. Six killed in Israeli airstrikes across Gaza [Wire]
23. Gaza health ministry declares a health emergency amid a sharp rise in
    meningitis cases [Wire]
24. Iraq seeks a higher oil output capacity estimate ahead of the 2027
    OPEC quota debate [Reuters]
25. China probes Shanghai party boss Chen Jining, the fourth Politburo
    member to fall since 2025 [Reuters]
26. US blacklists a Singapore Alibaba unit and six affiliated firms over
    alleged Nvidia chip diversion to China [Reuters]
27. Trump pardons Thanksgiving turkeys Freedom and Feathers [Reuters]
28. US consumer confidence jumps to its highest level in nearly two years
    [Reuters]
29. US CIA and ODNI suffer a cybersecurity breach involving some
    unclassified information [Reuters]
30. Fort Hood shooter Nidal Hasan seeks a stay of execution set for next
    week [Reuters]
31. US reports three human bird flu cases, one death, in Washington state
    [WHO via Reuters]
32. Argentina's economic activity declines in September for a third
    straight annual drop [Reuters]
33. Mexico reports 12 active measles cases, 90% of population vaccinated
    [Reuters]
34. US to host the Copa America for a second successive tournament in 2028
    [Reuters]
35. England beat Australia by 8 wickets in the 2nd T20I, levelling the
    series 1-1 [Press]
36. Real Madrid beat PSV 5-1; Bellingham scores a wonder goal [BBC]
37. Heavy fighting near a hospital in Ituri traps DR Congo Ebola
    responders [WHO]
38. Drones killed more than 1,600 people in Sudan this year, UN rights
    commission says [UN]
39. MSF suspends all activities in South Sudan's Yei River county
    following an abduction [MSF]
40. ECOWAS ministerial committee reviews preparations for the 2027 single
    currency launch [PANA]
41. Libya's frozen conflict risks a fresh flare-up after the port sinking
    — today's Reuters explainer on its fallout [Reuters]

### Left out on purpose (DATE CHECK)
- The US midterm elections (3 Nov 2026).
- Nvidia's +31.5% surge (Mon 23 Nov 2026).
- The Shenzhou-24 crew announcement (Tue 24 Nov 2026 — the launch was today).
- The Libyan port sinking itself (Sun 22 Nov 2026 — only today's explainer
  on its fallout is listed, as story 41).

## How the image was made
`build_image.py` renders the page with Python PIL from the story lists
above: masthead, dateline, lead, numbers strip, region bar, UTC timeline,
hero panels with flat vector illustrations drawn in code, the illustrated
grid, the briefs list, a dotted world map (dot grid clipped to coarse
continent outlines) with numbered pins 1–13, and the DATE CHECK / HOW SURE
footer. The output is a 1024x1024 PNG (185,391 bytes). `main.py`
(standard library only) copies it byte-for-byte to `/output/entry.png`;
two runs produce identical bytes.
