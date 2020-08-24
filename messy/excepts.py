#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
exceptions = [KeyError, KeyboardInterrupt, ConnectionResetError, ConnectionAbortedError, ConnectionRefusedError]

try:
    cls = random.choice(exceptions)
    raise cls(cls.__name__)
except KeyError as e:
    print(e)
except KeyboardInterrupt as e:
    print(e)
except (ConnectionResetError, ConnectionAbortedError, ConnectionRefusedError) as e:
    print(e)
except Exception as e:
    print(e)
