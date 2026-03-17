---
title: "How to solve error \"Failed to create file: about.html com.ibm.g11n.pipeline.client.ServiceException: Error while processing API request PUT ELM-ICL-prod/v2/files/about.html\"?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "access"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760075165"
source_url: "https://help.straker.ai/en/g11n/how-to-solve-error-failed-to-create-file-about.html-com.ibm.g11n.pipeline.client.serviceexception-error-while-processing-api-request-put-elm-icl-pro-1717479405684"
exported_at: "2026-03-17T11:32:05Z"
---

# How to solve error "Failed to create file: about.html com.ibm.g11n.pipeline.client.ServiceException: Error while processing API request PUT ELM-ICL-prod/v2/files/about.html"?

When using CLI command like this :

```
java -jar gpv2-java-tools-master/gp-java-tools/gp-cli/target/gp-cli-2.4.6-with-dependencies.jar create-file -f about.html -t text/html -l en,fr,de -j mycreds_icl_prod.json
```

If you got the error like this:

```
Failed to create file: about.html  
com.ibm.g11n.pipeline.client.ServiceException: Error while processing API request PUT ELM-ICL-prod/v2/files/about.html  
at com.ibm.g11n.pipeline.client.impl.ServiceClientImpl.invokeApiJson(ServiceClientImpl.java:2006)  
at com.ibm.g11n.pipeline.client.impl.ServiceClientImpl.invokeApiJson(ServiceClientImpl.java:1975)  
at com.ibm.g11n.pipeline.client.impl.ServiceClientImpl.createFile(ServiceClientImpl.java:676)  
at com.ibm.g11n.pipeline.tools.cli.CreateFileCmd._execute(CreateFileCmd.java:161)  
at com.ibm.g11n.pipeline.tools.cli.BaseCmd.execute(BaseCmd.java:106)  
at com.ibm.g11n.pipeline.tools.cli.FileCmd.execute(FileCmd.java:69)  
at com.ibm.g11n.pipeline.tools.cli.GPCmd.main(GPCmd.java:114)  
Caused by: javax.net.ssl.SSLHandshakeException: No subject alternative DNS name matching api.pipeline.g11n.ibm.com found.  
at sun.security.ssl.Alert.createSSLException(Alert.java:131)  
at sun.security.ssl.TransportContext.fatal(TransportContext.java:331)  
at sun.security.ssl.TransportContext.fatal(TransportContext.java:274)  
at sun.security.ssl.TransportContext.fatal(TransportContext.java:269)  
at sun.security.ssl.CertificateMessage$T12CertificateConsumer.checkServerCerts(CertificateMessage.java:654)  
at sun.security.ssl.CertificateMessage$T12CertificateConsumer.onCertificate(CertificateMessage.java:473)  
at sun.security.ssl.CertificateMessage$T12CertificateConsumer.consume(CertificateMessage.java:369)  
at sun.security.ssl.SSLHandshake.consume(SSLHandshake.java:377)  
at sun.security.ssl.HandshakeContext.dispatch(HandshakeContext.java:444)  
at sun.security.ssl.HandshakeContext.dispatch(HandshakeContext.java:422)  
at sun.security.ssl.TransportContext.dispatch(TransportContext.java:182)  
at sun.security.ssl.SSLTransport.decode(SSLTransport.java:152)  
at sun.security.ssl.SSLSocketImpl.decode(SSLSocketImpl.java:1401)  
at sun.security.ssl.SSLSocketImpl.readHandshakeRecord(SSLSocketImpl.java:1309)  
at sun.security.ssl.SSLSocketImpl.startHandshake(SSLSocketImpl.java:440)  
at sun.net.www.protocol.https.HttpsClient.afterConnect(HttpsClient.java:559)  
at sun.net.www.protocol.https.AbstractDelegateHttpsURLConnection.connect(AbstractDelegateHttpsURLConnection.java:197)  
at sun.net.www.protocol.http.HttpURLConnection.getOutputStream0(HttpURLConnection.java:1342)  
at sun.net.www.protocol.http.HttpURLConnection.getOutputStream(HttpURLConnection.java:1317)  
at sun.net.www.protocol.https.HttpsURLConnectionImpl.getOutputStream(HttpsURLConnectionImpl.java:264)  
at com.ibm.g11n.pipeline.client.impl.ServiceClientImpl.invokeApi(ServiceClientImpl.java:2062)  
at com.ibm.g11n.pipeline.client.impl.ServiceClientImpl.invokeApiJson(ServiceClientImpl.java:1991)  
... 6 more  
Caused by: java.security.cert.CertificateException: No subject alternative DNS name matching api.pipeline.g11n.ibm.com found.  
at sun.security.util.HostnameChecker.matchDNS(HostnameChecker.java:230)  
at sun.security.util.HostnameChecker.match(HostnameChecker.java:106)  
at sun.security.ssl.X509TrustManagerImpl.checkIdentity(X509TrustManagerImpl.java:463)  
at sun.security.ssl.X509TrustManagerImpl.checkIdentity(X509TrustManagerImpl.java:423)  
at sun.security.ssl.X509TrustManagerImpl.checkTrusted(X509TrustManagerImpl.java:230)  
at sun.security.ssl.X509TrustManagerImpl.checkServerTrusted(X509TrustManagerImpl.java:129)  
at sun.security.ssl.CertificateMessage$T12CertificateConsumer.checkServerCerts(CertificateMessage.java:638)
```

Please check if you are point to the Straker host (https://g11n-pipeline-api.straker.global/translate/rest) in your `mycreds_icl_prod.json` credential file.
