# NOTES — THE WORLD, Wednesday 25 November 2026 (v2)

A broadsheet front page summing up Wednesday 25 November 2026 in one
image: 37 stories (1 lead + 36 grouped by region) across 6 continents,
plus a schematic world map marking where the news happened.

Every story below was first reported on 25 November 2026 (in some cases
late on 24 November UTC, reported in the 25 November wires and summaries).
Nothing here is invented, hyped, or speculative: each line states what was
reported, with the numbers as reported.

## Stories and sources

### Lead
- Ukraine confirms drone strike on Russian cargo ship in the Gulf of
  Finland — President Zelenskiy confirms responsibility; 16 crew
  evacuated, ship towed to St Petersburg; Norway urges caution.
  Source: Reuters world news summary, 25 Nov 2026
  (devdiscourse.com/article/international/4011704-reuters-world-news-summary).

### Europe (8)
1. Russian attack kills 2, wounds 22 in Zaporizhzhia — Reuters.
2. Putin: Ukraine keeps striking oil refineries despite Trump's requests;
   Russia will respond — Reuters, 24–25 Nov 2026.
3. Latvian president Rinkevics sees a possible "tipping point" in the
   Ukraine war next year — Reuters.
4. French officials order ex-president Sarkozy's corruption case (with
   wife Carla Bruni) to trial; pre-trial hearing 1 April 2027 — Reuters.
5. Swedish PM Andersson fails again in her bid to form a government —
   Euronews-style wire summary, 25 Nov 2026.
6. Ukraine sank a Russian naval vessel in a Libyan port — AAP/Reuters.
7. NATO chief promises safeguarding against space threat after reports of
   Russian nuclear satellites — wire summary, 25 Nov 2026.
8. Norway urges Kyiv to exercise caution in such operations — Reuters.

### Middle East (7)
9. Houthis hit Riyadh's tallest tower, 11 wounded — second strike within
   days — Saudi Civil Defence via Reuters/Al Jazeera.
10. Houthis push to within 60 km of Aden; Yemeni military says they will
    not seize the city — Reuters.
11. Houthis report 25 dead or missing in Saudi airstrikes in southern
    Yemen — wire summary, 25 Nov 2026.
12. Israeli airstrikes kill Naim Abu Nahl, Hamas-run interior ministry
    security chief, west of Gaza City — AP, 24 Nov 2026.
13. Six killed in Israeli airstrikes across Gaza — Palestinian emergency
    services, 25 Nov 2026.
14. Gaza health ministry declares a health emergency amid a sharp rise in
    meningitis cases; WHO deputy chief: "no excuse for inaction" — wire
    summaries, 25 Nov 2026.
15. Iraq seeks a higher oil output capacity estimate ahead of the 2027
    OPEC quota debate — Reuters.

### Asia-Pacific (7)
16. China launches Shenzhou-24: Pakistani astronaut Muhammad Zeeshan Ali,
    40, becomes the first Pakistani in orbit and the first foreign
    astronaut aboard Tiangong; crew Tang Hongbo and Wu Yi; launch 08:18
    Beijing time from Jiuquan — Reuters/AP/Xinhua, 25 Nov 2026.
17. China's Huawei convicted in sprawling US criminal trial over Iran
    business; guilty on trade secrets, acquitted of racketeering —
    Reuters/BBC.
18. China probes Shanghai party boss Chen Jining, the fourth Politburo
    member to fall since 2025 — Reuters.
19. Magnitude 5.6 earthquake strikes Nepal's Koshi province near the
    China border — EMSC via wire summary, 24–25 Nov 2026.
20. Asian stocks tumble on fresh US tariff threats: Korea down 5.3%,
    Taiwan down 5.1%, Nikkei down 2.9% — Reuters, 25 Nov 2026.
21. US blacklists a Singapore Alibaba unit and six affiliated firms over
    alleged Nvidia chip diversion to China — Reuters.
22. Vaibhav Sooryavanshi, 15, smashes 204 off 53 balls for India A against
    UAE, a record double century — press reports, 24–25 Nov 2026.

### Americas (9)
23. Trump awards Rudy Giuliani the Presidential Medal of Freedom — Reuters.
24. Trump pardons Thanksgiving turkeys Freedom and Feathers — Reuters.
25. Dow closes above 50,000 at 50,018.70 (+0.85%); Nasdaq falls 1.48% as
    Nvidia slides 5.9% — market reports, 24 Nov 2026 close.
26. Dell reports doubled sales of $54.9bn and $60.2bn in new AI server
    orders; shares rise 4.1% after hours — Reuters.
27. US consumer confidence jumps to its highest level in nearly two years —
    Reuters.
28. US CIA and ODNI suffer a cybersecurity breach involving some
    unclassified information — Reuters, citing a source.
29. Fort Hood shooter Nidal Hasan seeks a stay of execution set for next
    week — US court records via Reuters.
30. US reports three human bird flu cases, one death, in Washington state
    — WHO via Reuters.
31. US to host the Copa America for a second successive tournament in 2028
    — Reuters.

### Africa (5)
32. Libya's frozen conflict risks fresh instability after Ukraine's sinking
    of a Russian vessel in a Libyan port — Reuters explainer.
33. Heavy fighting near a hospital in Ituri traps DR Congo Ebola
    responders — WHO via PANA, 23–25 Nov 2026.
34. Drones killed more than 1,600 people in Sudan this year — UN rights
    commission via PANA.
35. MSF suspends all activities in South Sudan's Yei River county
    following an abduction — MSF/PANA, 24 Nov 2026.
36. ECOWAS ministerial committee reviews preparations for the 2027 single
    currency launch — PANA, 24 Nov 2026.

## How the image was made
`build_image.py` renders the page with Python PIL from the story list
above: masthead, dateline, lead, a schematic world map drawn from coarse
continent outlines with the story locations marked, and the 36 stories
grouped under five region headers. The output is a 1024x1024 PNG
(210,930 bytes). `main.py` (standard library only) copies it byte-for-byte
to `/output/entry.png`; two runs produce identical bytes.
