emails = {'mgu.edu': ['stepan_socolov', 'firsov_kirill', 'filip_kirkorov', 'polya_k'],
      	'gmail.com': ['shary.oficcial', 'olegLSP.oficcial', 'mr.beast'],
      	'msu.edu': ['ivan_ivanov', 'petr_petrov', 'joseph_joestar'],
      	'yandex.ru': ['katya_smirnova', 'gleb_alexandrovich'],
      	'harvard.edu': ['miron.yanovich', 'mark.zuckerberg', 'jonathan.joestar'],
      	'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
print(*sorted({i + '@' + k for k, v in emails.items() for i in v}), sep = '\n')