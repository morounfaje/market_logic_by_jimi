# Market Logic by Jimi

Python projects built on a 72-week road to becoming a quantitative trading engineer. Every week I build one working tool, and this repo is the public record of it, from first script to deployed system.

**Goal:** design, test, and deploy automated trading systems, and work in quantitative and algorithmic trading.

---

## The 72-Week Roadmap

| Phase | Weeks | Focus |
|-------|-------|-------|
| **1. Python for Trading** | 1-36 | Core Python, NumPy/Pandas, backtesting, order management, bots, APIs, Docker, VPS deployment |
| **1B. Quant Statistics and ML** | 1-24 (concurrent) | Probability, inference, GARCH, Monte Carlo, XGBoost, LSTM, leak-free validation |
| **2. MQL5 and MetaTrader 5** | 13-48 (parallel) | Expert Advisors, risk management, live deployment on a VPS |
| **3. Financial Theory** | 37-54 | Portfolio theory, factor models, Black-Scholes, market microstructure |
| **4. AI / LLM Engineering** | 55-72 | RAG, agents, LLM sentiment signals, fine-tuning, production serving |

Along the way I build five flagship systems: an automated Python alpha engine, an MT5 EA suite, a quant research system, an institutional-style research report, and an AI intelligence layer.

I am currently in **Phase 1, Python for Trading**.

---

## Progress

| Week | Project | Skills |
|------|---------|--------|
| 1 | [P&L Calculator](#week-1-pl-calculator) | input, operators, conditionals, loops |
| 2 | [Trade Guess Game](#week-2-trade-guess-game) | functions, loops, randomness, session tracking |
| 3 | [Grading System](#week-3-grading-system) | functions, `*args`, default arguments, lambda |
| 4 | [Trade Logger](#week-4-trade-logger) | lists, dicts, sets, comprehensions |
| 5 | Coming soon | files and error handling |

---

## Week 1: P&L Calculator

**File:** `1_pnl_calculator_cli.py`
**Run:** `python 1_pnl_calculator_cli.py`

A command-line calculator for a single trade. Enter entry price, exit price, shares, commission, stop loss, and direction (long or short). It returns gross P&L, net P&L after commission, percentage return, a WIN / LOSS / BREAKEVEN verdict, and the risk-to-reward ratio. It rejects invalid stops and invalid directions, and loops so you can check several trades in a row.

**Skills:** `input()`, type conversion, `if/elif/else`, `while` loops, f-string formatting, long vs short logic.

**Next improvement:** handle non-numeric input without crashing, using `try/except`.

---

## Week 2: Trade Guess Game

**File:** `2_trade_guess_game_v4.py`
**Run:** `python 2_trade_guess_game_v4.py`

A number-guessing game dressed as trading: guess a hidden P&L. Three difficulty levels change the range and the number of guesses. Each wrong guess returns a hot/warm/cold hint and a higher/lower direction. The game scores each win and prints a session summary (games played, win rate, total score).

**Skills:** functions with return values, `random`, nested loops, `break`, session accumulators, `abs()`.

**Next improvement:** handle non-numeric input without crashing, using `try/except`.

---

## Week 3: Grading System

**File:** `3_grading_system_v3.py`
**Run:** `python 3_grading_system_v3.py`

A small trade-analysis toolkit over a list of trades (EURUSD, GBPUSD, XAUUSD, USDJPY). It totals P&L, calculates position size from account balance and a risk percentage, filters the winning trades, and ranks all trades from best to worst.

**Skills:** `*args`, default arguments, `filter()` with `lambda`, `sorted()` with a `lambda` key, lists of dictionaries.

**Next improvement:** compute the total from the trades list itself instead of typing the numbers twice.

---

## Week 4: Trade Logger

**File:** `4_csv_trade_logger_v2.py`
**Run:** `python 4_csv_trade_logger_v2.py`

A menu-driven trade logger. Log trades (long or short), view all trades, rank them by P&L, filter by ticker, and see a session summary: trade count, win rate, total, best and worst trade, and tickers traded. A blacklist set rejects unwanted tickers such as MEME, SCAM, and FAKE.

**Skills:** lists of dicts, sets for blacklisting and unique tickers, list and set comprehensions, `enumerate()`, `sorted()` with `lambda`, menu loops.

**Next improvement (Week 5):** save trades to a real CSV file and reload them on startup, which is the file handling topic of the next week.

---

## How to run any project

1. Install Python 3.11 or newer.
2. Clone the repo:
   ```
   git clone https://github.com/morounfaje/market_logic_by_jimi.git
   cd market_logic_by_jimi
   ```
3. Run a project with `python <filename>`.

---

## About

Built by Jimi Yusuf, based in Nigeria, working toward a career in quantitative trading and algorithmic systems. I publish what I build as I build it, including the mistakes.
