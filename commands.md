
# Free Fire Bot - Complete Commands Documentation

## System Overview
This bot is designed for Free Fire game integration with private chat commands, squad management, and emote system.

---

## Core Configuration Files

### 1. config_manager.py
Manages persistent storage using JSON for:
- Multiple owner UIDs (unlimited)
- Custom emote commands
- All data persists in `config.json`

### 2. message_formatter.py
Handles all response formatting with:
- Random crystal colors for dark backgrounds
- Professional and friendly tone
- Proper alignment and spacing
- Instagram footer branding

---

## All Available Commands

### 1. **Secret Toggle Command** (Private Only)
**Command:** `/stop/896422`

**Purpose:** Toggle group responses ON/OFF

**Working:**
- Only works in private chat (DD check: `chatdata['5']['data']['16']`)
- Toggles `group_responses_enabled` variable
- Changes bot behavior in squad/clan chats
- No response sent (secret command)

**Implementation:**
```python
if inPuTMsG == '/stop/896422':
    try:
        dd = chatdata['5']['data']['16']  # Check private
        group_responses_enabled = not group_responses_enabled
        status = "OFF" if not group_responses_enabled else "ON"
        print(f' 🔒 Secret: Group responses {status}')
    except:
        pass
```

---

### 2. **Status Check Command** (Private Only)
**Command:** `/89`

**Purpose:** Check if group responses are enabled or disabled

**Response Format:**
```
[Random Color]🔍 Status Check
[Random Color]━━━━━━━━━━━━━━━
[Random Color]Group Responses: ON/OFF
[Random Color]━━━━━━━━━━━━━━━
```

**Working:**
- Private chat only
- Shows current state of `group_responses_enabled`

---

### 3. **Help Command** (All Chats)
**Command:** `/help`

**Purpose:** Show all available commands

**Response:** Two-part message with delay

**Part 1:**
```
[B][C][Random Color] 
[Random Color]  COMMAND GUIDE
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color] Here is what I can help you with
[Random Color] ㅤ
[Random Color] Squad Commands:
[Random Color] ㅤ
[Random Color] /5 - Accept squad invite
[Random Color] ㅤ
[Random Color] /x/[code] - Join squad
[Random Color] ㅤ
[Random Color] leave - Exit squad
[Random Color] 
[Random Color]--------------------
[Random Color] 
```

**Part 2 (after 0.5s delay):**
```
[B][C][Random Color] 
[Random Color]  SPECIAL COMMANDS
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color] /spm/[times]/[uid] - Send invites
[Random Color] ㅤ
[Random Color] /s - Special function
[Random Color] ㅤ
[Random Color] @a [uid] [emote] - Emote attack
[Random Color] ㅤ
[Random Color] Feel free to use any command
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color]Follow on Instagram
[Random Color]@1onlysarkar
[Random Color] 
```

**Behavior:**
- Responds in all chats if `group_responses_enabled = True`
- Always responds in private chat (chat_type = 2)

---

### 4. **Greeting Commands** (All Chats)
**Commands:** `hi`, `hello`, `fen`, `salam`

**Response:**
```
[B][C][Random Color] 
[Random Color]  WELCOME FRIEND
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color] Hey there
[Random Color] 
[Random Color] I am your Free Fire assistant
[Random Color] here to help you out
[Random Color] 
[Random Color] Type /help to see what I can do
[Random Color] for you
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color]Follow on Instagram
[Random Color]@1onlysarkar
[Random Color] 
```

**Behavior:**
- Same as `/help` - respects `group_responses_enabled`

---

### 5. **Squad Invite Accept** (Private Only)
**Command:** `/5`

**Purpose:** Accept squad invitation and send invite to user

**Response:**
```
[B][C][Random Color] 
[Random Color]  SQUAD INVITATION
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color] Hey I have sent you an invite
[Random Color]  
[Random Color] Please accept it quickly so we
[Random Color] can team up together
[Random Color]  
[Random Color] Thanks
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color]Follow on Instagram
[Random Color]@1onlysarkar
[Random Color] 
```

**Working:**
1. Opens squad
2. Changes squad to 5 members
3. Sends invite to user
4. Exits squad after 3 seconds

---

### 6. **Join Squad with Code** (Private Only)
**Command:** `/x/{code}`

**Example:** `/x/5911500`

**Purpose:** Join a squad using squad code

**Working:**
- Generates join squad packet with provided code
- Sends to online server

---

### 7. **Spam Invites** (Private Only)
**Command:** `/spm/{times}/{uid}`

**Example:** `/spm/10/4223188434`

**Response:**
```
[B][C][Random Color] 
[Random Color]  INVITES SENDING
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color] Starting invitation process
[Random Color]  
[Random Color] Total Invites: 10
[Random Color] Target Player: 4🗿223🗿188🗿434
[Random Color]  
[Random Color] Please wait while I send them
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color]Follow on Instagram
[Random Color]@1onlysarkar
[Random Color] 
```

**Working:**
- Opens squad
- Loops {times} times:
  - Changes squad settings
  - Sends invite to {uid}
  - Exits and reopens squad
  - 0.15-0.2s delays between actions

---

### 8. **Leave Squad** (All Chats)
**Command:** `leave`

**Purpose:** Exit current squad

---

### 9. **Special Function** (All Chats)
**Command:** `/s`

**Purpose:** FS (Friend System) function

---

### 10. **Emote Attack** (All Chats)
**Command:** `@a {uid} {uid2} {uid3} {uid4} {uid5} {emote_id}`

**Example:** `@a 4223188434 909000001`

**Response:**
```
[B][C][Random Color] 
[Random Color]  TARGET LOCKED
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color] Target activated successfully
[Random Color]  
[Random Color] Player ID: 4🗿223🗿188🗿434
[Random Color]  
[Random Color] Ready to execute command
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color]Follow on Instagram
[Random Color]@1onlysarkar
[Random Color] 
```

**Working:**
- Sends emote to up to 5 different UIDs
- Uses last number as emote ID

---

### 11. **Set Owner UIDs** (Private Only)
**Command:** `/uid/{uid1}/{uid2}/{uid3}/...`

**Example:** `/uid/4223188434/1234567890/9876543210/`

**Response:**
```
[B][C][Random Color]Owner UID Set
[Random Color]--------------------
[Random Color] 
[Random Color]Successfully set 3
[Random Color]owner UID(s)
[Random Color] 
[Random Color]4🗿223🗿188🗿434
[Random Color]1🗿234🗿567🗿890
[Random Color]9🗿876🗿543🗿210
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color]Follow on Instagram
[Random Color]@1onlysarkar
```

**Working:**
- Splits UIDs by `/`
- Saves all UIDs to `config.json` via `config_manager.set_owner_uids()`
- Unlimited UIDs supported

---

### 12. **Create Emote Command** (Private Only)
**Command:** `/e/{name}/{emote_code}`

**Example:** `/e/ak/909000063`

**Response:**
```
[B][C][Random Color]Emote Command Saved
[Random Color]--------------------
[Random Color] 
[Random Color]Command /ak
[Random Color]saved successfully with
[Random Color]emote 909000063
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color]Follow on Instagram
[Random Color]@1onlysarkar
```

**Working:**
- Saves emote with name to `config.json`
- Accessible via `/{name}` command

---

### 13. **Remove Emote Command** (Private Only)
**Command:** `/rmv/{name}`

**Example:** `/rmv/ak`

**Response (Success):**
```
[B][C][Random Color]Emote Removed
[Random Color]--------------------
[Random Color] 
[Random Color]Command /ak
[Random Color]removed successfully
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color]Follow on Instagram
[Random Color]@1onlysarkar
```

**Response (Not Found):**
```
[B][C][Random Color]Emote Not Found
[Random Color]--------------------
[Random Color] 
[Random Color]Command /ak
[Random Color]does not exist
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color]Follow on Instagram
[Random Color]@1onlysarkar
```

**Working:**
- Removes emote command from `config.json`
- Returns success/failure status

---

### 14. **List All Emotes** (Private Only)
**Command:** `/emt`

**Purpose:** Show all saved emote commands

**Response:** Multiple messages in chunks of 10
```
/p90 /dr /thr /flg /ak /scar /cbr1 /cbr2 /cbr3 /cbr4
/cobra /m10 /xm8 /fms /ump /boyah /boyah2 /m4 /mp5 /rmp
...
```

**Working:**
- Gets all emotes from `config_manager.get_all_emotes()`
- Sends 10 commands per message
- 0.3s delay between messages
- Plain format, no borders

---

### 15. **Execute All Emotes** (Private Only)
**Command:** `/all/{seconds}`

**Example:** `/all/2`

**Start Response:**
```
[B][C][Random Color]Starting All Emotes
[Random Color]--------------------
[Random Color] 
[Random Color]Executing 34 emotes
[Random Color]Interval: 2.0s
[Random Color]UIDs: 4
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color]Follow on Instagram
[Random Color]@1onlysarkar
```

**Per Emote Response:**
```
[B][C][Random Color]Emote Executed
[Random Color]--------------------
[Random Color] 
[Random Color]Name: /ak
[Random Color]Code: 909000063
[Random Color] 
[Random Color]--------------------
```

**End Response:**
```
[B][C][Random Color]All Emotes Completed
[Random Color]--------------------
[Random Color] 
[Random Color]Total: 34 emotes
[Random Color]Executed successfully
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color]Follow on Instagram
[Random Color]@1onlysarkar
```

**Working:**
1. Gets all saved emotes and owner UIDs
2. Loops through each emote
3. Sends emote to ALL UIDs simultaneously using `asyncio.gather()`
4. Waits {seconds} before next emote
5. Sends response after each emote

**Error Responses:**
- No UIDs set: Shows UID setup instruction
- No emotes: Shows add emotes instruction

---

### 16. **Execute Custom Emote** (Private Only)
**Command:** `/{name}`

**Example:** `/ak`

**Response (Success):**
```
[B][C][Random Color]Sent Successfully
[Random Color]--------------------
[Random Color] 
[Random Color]Sent successfully
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color]Follow on Instagram
[Random Color]@1onlysarkar
```

**Response (No UID):**
```
[B][C][Random Color]UID Not Found
[Random Color]--------------------
[Random Color] 
[Random Color]No UID found
[Random Color]Please set using
[Random Color]/uid/{uid}
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color]Follow on Instagram
[Random Color]@1onlysarkar
```

**Response (Command Not Found):**
```
[B][C][Random Color]Command Not Found
[Random Color]--------------------
[Random Color] 
[Random Color]Command not found
[Random Color]Please create it using
[Random Color]/e/{name}/{emote}
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color]Follow on Instagram
[Random Color]@1onlysarkar
```

**Working:**
- Gets saved emote code from config
- Sends to ALL saved UIDs simultaneously using `asyncio.gather()`
- Much faster than sequential execution

---

### 17. **Emote Sequence** (Private Only)
**Command:** `/{name}.{seconds}/{name}.{seconds}/{name}.{seconds}/...`

**Example:** `/ak.2/m10.3/thompson.1.5/`

**Start Response:**
```
[B][C][Random Color]Starting Sequence
[Random Color]--------------------
[Random Color] 
[Random Color]Executing 3 emotes
[Random Color]UIDs: 4
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color]Follow on Instagram
[Random Color]@1onlysarkar
```

**Per Emote Response:**
```
[B][C][Random Color]Emote Executed
[Random Color]--------------------
[Random Color] 
[Random Color]Name: /ak
[Random Color]Code: 909000063
[Random Color]Duration: 2.0s
[Random Color] 
[Random Color]--------------------
```

**End Response:**
```
[B][C][Random Color]Sequence Completed
[Random Color]--------------------
[Random Color] 
[Random Color]Total: 3 emotes
[Random Color]Executed successfully
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color]Follow on Instagram
[Random Color]@1onlysarkar
```

**Working:**
1. Parses sequence: splits by `/`
2. Each part: `{name}.{timing}`
3. Validates each emote exists
4. Executes sequentially with custom timing
5. Sends to ALL UIDs simultaneously per emote
6. Unlimited emotes in sequence

**Error Response:**
```
[B][C][Random Color]Invalid Sequence
[Random Color]--------------------
[Random Color] 
[Random Color]No valid emotes found
[Random Color]Format:
[Random Color]/{name}.{sec}/{name}.{sec}/
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color]Follow on Instagram
[Random Color]@1onlysarkar
```

---

## Command Exclusions

Custom emote commands (`/{name}`) do NOT trigger when command starts with:
- `/uid/`
- `/e/`
- `/rmv/`
- `/help`
- `/5`
- `/x/`
- `/spm/`
- `/s`
- `/stop/`
- `/89`
- `/emt`
- `/all/`

---

## Auto Squad Welcome Message

**When bot joins squad (squad invite accepted):**

```
[B][C][Random Color] 
[Random Color]  BOT ACTIVE
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color] Hello everyone
[Random Color]  
[Random Color] I am now active and ready to
[Random Color] assist you
[Random Color]  
[Random Color] Squad Owner: {owner_uid}
[Random Color]  
[Random Color] Type /help to see all available
[Random Color] commands and features
[Random Color]  
[Random Color] Let us have a great game
[Random Color] 
[Random Color]--------------------
[Random Color] 
[Random Color]Follow on Instagram
[Random Color]@1onlysarkar
[Random Color] 
```

**Behavior:**
- Only sends if `group_responses_enabled = True`

---

## Color System

### Crystal Colors (65 colors)
Used for all responses, optimized for dark backgrounds:
- Cyan, Spring Green, Dodger Blue
- Royal Blue, Medium Purple, Hot Pink
- Orange, Gold, Lime Green, Turquoise
- And 55 more vibrant colors

### Random Color Selection
Each response gets a new random color from `CRYSTAL_COLORS` list.

---

## Message Formatting

All messages use `message_formatter.py` with:

```python
format_message(title, content, footer="Follow on Instagram\n@1onlysarkar")
```

**Structure:**
1. Top spacing
2. Title (centered, uppercase)
3. Separator line (20 dashes)
4. Content (with proper spacing)
5. Bottom separator
6. Footer (Instagram branding)
7. Bottom spacing

**Prefix:** `[B][C]` (Bold + Center alignment)

---

## UID Formatting

Function: `xMsGFixinG(uid)`

**Format:** Adds 🗿 emoji every 3 digits

**Example:**
- Input: `4223188434`
- Output: `4🗿223🗿188🗿434`

---

## Persistence (config.json)

### Structure:
```json
{
  "owner_uids": [
    "4223188434",
    "1234567890",
    "9876543210"
  ],
  "emotes": {
    "p90": "909049010",
    "dr": "909050009",
    "ak": "909000063",
    "m10": "909000081"
  }
}
```

### Functions:
- `set_owner_uids(uids_list)` - Save UIDs
- `get_owner_uids()` - Get all UIDs
- `add_emote(name, code)` - Save emote
- `get_emote(name)` - Get single emote
- `get_all_emotes()` - Get all emotes dict
- `remove_emote(name)` - Remove emote (returns True/False)

---

## Critical Implementation Notes

### 1. Private Chat Detection
```python
dd = chatdata['5']['data']['16']  # Throws error if not private
```

### 2. Group Response Control
```python
if group_responses_enabled or response.Data.chat_type == 2:
    # Send response
```
- `chat_type = 0` → Squad
- `chat_type = 1` → Clan  
- `chat_type = 2` → Private (always responds)

### 3. Simultaneous UID Execution
```python
tasks = []
for saved_uid in saved_owner_uids:
    H = await Emote_k(int(saved_uid), int(emote_code), key, iv, region)
    tasks.append(SEndPacKeT(whisper_writer, online_writer, 'OnLine', H))
await asyncio.gather(*tasks)
```
Uses `asyncio.gather()` for parallel execution.

### 4. Region-Based Packet Headers
Handled in `xC4.py`:
```python
if region.lower() == "ind":
    packet = '0514'
elif region.lower() == "bd":
    packet = "0519"
else:
    packet = "0515"
```

---

## Example Emote Database

```python
emotes = {
    "p90": "909049010",
    "dr": "909050009",
    "thr": "909000014",
    "flg": "909000034",
    "ak": "909000063",
    "scar": "909000068",
    "cbr1": "909000071",
    "cbr2": "909000072",
    "cbr3": "909000073",
    "cbr4": "909000074",
    "cobra": "909000075",
    "m10": "909000081",
    "xm8": "909000085",
    "fms": "909000090",
    "ump": "909000098",
    "boyah": "909000124",
    "boyah2": "909000125",
    "m4": "909033001",
    "mp5": "90903302",
    "rmp": "909034003",
    "sx": "909034009",
    "shotgun": "909035007",
    "jb": "909035010",
    "an91": "909035012",
    "thompson": "909038010",
    "g80": "909038012",
    "m102": "909039011",
    "mp402": "909040010",
    "groza": "909041005",
    "100": "909042007",
    "wpkr": "909042008",
    "prfl": "909045001",
    "clap": "909049008",
    "map": "909050014"
}
```

---

## Restoration Instructions

### To restore complete system:

1. **Copy all files:**
   - `saurabh.py` (main bot)
   - `config_manager.py` (persistence)
   - `message_formatter.py` (responses)
   - `xC4.py` (encryption/packets)
   - `xHeaders.py` (utilities)
   - All `Pb2/*.py` (protobuf files)

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set bot credentials in saurabh.py:**
   ```python
   Uid, Pw = '4223188434', '3E7FFB26E53336EFD07763252D70E8E400E88E11BA5EEDE80F0CDCE6E28EFD2E'
   ```

4. **Restore saved data (if available):**
   - Copy `config.json` with all UIDs and emotes

5. **Run bot:**
   ```bash
   python saurabh.py
   ```

---

## Developer Credits

- **Original System:** REDZED
- **Emote System:** PARAHEX X CODEX
- **Instagram:** @1onlysarkar
- **Platform:** Replit

---

## Version History

- **v1.0** - Initial bot with squad commands
- **v2.0** - Added persistent config system
- **v3.0** - Added multiple UID support (unlimited)
- **v4.0** - Added `/emt` command (list emotes)
- **v5.0** - Added `/all/{seconds}` command (execute all emotes)
- **v6.0** - Added sequence command `/{name}.{sec}/...`
- **v7.0** - Optimized UID execution (simultaneous via asyncio.gather)
- **v7.1** - Added `/rmv/{name}` command to remove emote commands

---

**Last Updated:** 2025-01-18
**Documentation Version:** 7.1
