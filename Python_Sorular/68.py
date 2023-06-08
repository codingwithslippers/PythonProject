# Exception handling nedir ve hangi durumlarda kullanılır?

"""
Exception handling (istisna işleme), bir programın çalışması sırasında ortaya çıkabilecek hataları ele almak ve bu hatalara uygun bir şekilde yanıt vermek için kullanılan bir programlama yaklaşımıdır. Python ve diğer birçok programlama dilinde, hatalar (istisnalar) bir exception olarak adlandırılır ve bu exception'lar programın normal akışını kesintiye uğratabilir.

Exception handling, programların hata durumlarıyla başa çıkmasına yardımcı olur. Bu hatalar, dosya işlemleri sırasında hatalar, ağ bağlantı sorunları, veri dönüşüm hataları, hatalı girişler gibi çeşitli durumlar olabilir. Exception handling kullanarak, programlarımızı daha güvenilir hale getirebiliriz, istenmeyen hatalardan koruyabiliriz ve hata durumlarında programın kontrolünü ele alabiliriz.

"""

"""

Exception handling, aşağıdaki durumlarda kullanılır:

1-Bir hata oluştuğunda programın çökmesini önlemek: Eğer bir hata meydana gelirse, exception handling kullanarak programın çökmesini engelleyebilir ve hatayı kontrol edebiliriz.

2-Hatanın nedenini tespit etmek ve kaydetmek: Exception handling, hatanın türünü ve ayrıntılarını yakalayarak, hatayı kaydedebilir veya bir log dosyasına yazabiliriz. Böylece, hata ayıklama ve sorun giderme için gerekli bilgileri elde edebiliriz.

3-Alternatif işlemler gerçekleştirmek: Hata durumunda alternatif bir işlem gerçekleştirebiliriz. Örneğin, bir dosya okunamazsa, başka bir dosya kullanabiliriz veya kullanıcıya bir hata mesajı gösterebiliriz.

4-Kaynakları düzgün bir şekilde serbest bırakmak: Exception handling, kaynakların (dosyalar, veritabanı bağlantıları, ağ bağlantıları vb.) düzgün bir şekilde serbest bırakılmasını sağlar. Bu, programın kaynakları kullanırken veya hatalar oluştuğunda kaynakları serbest bırakması için güvence sağlar.

Özetle, exception handling, programların hata durumlarıyla başa çıkmasını sağlayan bir mekanizmadır. Hataları yakalamak, işlemek ve uygun bir şekilde yanıt vermek için kullanılır. Böylece programlar daha güvenilir, daha esnek ve daha kullanıcı dostu hale gelir.

"""