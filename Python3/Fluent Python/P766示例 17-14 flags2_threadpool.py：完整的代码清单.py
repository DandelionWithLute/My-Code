import collections
from concurrent import futures

import requests
import tqdm

from flags2_common import main, HTTPStatus ➋
from flags2_sequential import download_one ➌
DEFAULT_CONCUR_REQ = 30 ➍
MAX_CONCUR_REQ = 1000 ➎
def download_many(cc_list, base_url, verbose, concur_req):
counter = collections.Counter()
with futures.ThreadPoolExecutor(max_workers=concur_req) as executor: ➏
to_do_map = {} ➐
for cc in sorted(cc_list): ➑
future = executor.submit(download_one,
cc, base_url, verbose) ➒
to_do_map[future] = cc ➓
done_iter = futures.as_completed(to_do_map) ⓫
if not verbose:
done_iter = tqdm.tqdm(done_iter, total=len(cc_list)) ⓬
for future in done_iter: ⓭
try:
res = future.result() ⓮
except requests.exceptions.HTTPError as exc: ⓯
error_msg = 'HTTP {res.status_code} - {res.reason}'
error_msg = error_msg.format(res=exc.response)
except requests.exceptions.ConnectionError as exc:
error_msg = 'Connection error'
else:
error_msg = ''
status = res.status
if error_msg:
status = HTTPStatus.error
counter[status] += 1
if verbose and error_msg:
cc = to_do_map[future] ⓰
print('*** Error for {}: {}'.format(cc, error_msg))
return counter
if __name__ == '__main__':
main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)

