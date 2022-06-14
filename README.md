<h1 align="center"> RuleDump </h1> <br>

<p align="center">
  <a href="https://github.com/famat-thesis/ruledump">
    <img alt="RuleDump" title="RuleDump" src="https://raw.githubusercontent.com/famat-thesis/ruledump/main/img/cover.jpg" width="450">
  </a>
</p>
<h2 align="center">
 From tabular DB to Rules, with one command line.
  </h2>


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Feedback](#feedback)
- [Acknowledgments](#acknowledgments)

## Introduction

### Usage
```sh
pip install ruledump

ruledump mydb.sqlite3

ruledump -c config.ini

ruledump --runexample y
```

### Database
<b> ruledump </b> is compatible with all SQL databases and knowledge bases (triples, turtle format).
### Rule
We define our rules as <a href=https://en.wikipedia.org/wiki/Tuple-generating_dependency > Tuple-generating dependency </a> (TGD).
<br>
For instance, we can mine "IF client A and client B have access to the same account then client A and client B have the same type of credit card."

## Features
- Find all the best rules in a <b>tabular</b> database.
- Works on any kind of databases with one pip install.
- Able to download and mine rules with one command line and one configuration file.

## Feedback
You can :
- Submit an issue / Pull request on github
- Contact us directly via email

## Acknowledgments  
Thanks to Telecom Paris and Hi! Paris for sponsoring this project.

<p align="center">
<a href=https://www.telecom-paris.fr/>
    <img alt="Telecom paris" title="Telecom paris logo" src="https://raw.githubusercontent.com/famat-thesis/ruledump/main/img/logo_telecom_ipparis.png" width="450">
  </a>


</p>

<p align="center">
  <a href="https://www.hi-paris.fr/">     <img alt="Hi! paris" title="Hi! paris logo" src="https://raw.githubusercontent.com/famat-thesis/ruledump/main/img/hiparis.png" width="450"></a>
</p>
