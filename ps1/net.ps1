$uri = "https://www.google.co.jp"
# $response = Invoke-WebRequest -Uri $uri
# $response

function getMpc(){
    Add-Type -AssemblyName 'System.Net.Http'
    # $multipartContent = [System.Net.Http.MultipartFormDataContent]::new()
    # $stringHeader = [System.Net.Http.Headers.ContentDispositionHeaderValue]::new("form-data")
    # $StringContent = [System.Net.Http.StringContent]::new("TestValue")
    $multipartContent = New-Object System.Net.Http.MultipartFormDataContent

    $stringHeader = New-Object System.Net.Http.Headers.ContentDispositionHeaderValue("form-data")
    $stringHeader.Name = "TestHeader"
    $StringContent = New-Object System.Net.Http.StringContent("TestValue")
    $StringContent.Headers.ContentDisposition = $stringHeader
    $multipartContent.Add($stringContent)
    
    $stringHeader = New-Object System.Net.Http.Headers.ContentDispositionHeaderValue("form-data")
    $stringHeader.Name = "TestHeader2"
    $StringContent = New-Object System.Net.Http.StringContent("TestValue2")
    $StringContent.Headers.ContentDisposition = $stringHeader
    $multipartContent.Add($stringContent)
    return ,$multipartContent
}

$mpc = getMpc
<#
$mpc.headers
$mpc.headers.key        # Content-Type
$mpc.headers.value      # multipart/form-data; boundary="8a346998-482d-4d3e-953c-c36860d12f2c"
($mpc | select -index 0).headers
($mpc | select -index 0).headers.key[0]     # Content-Type
($mpc | select -index 0).headers.key[1]     # Content-Length   <- 突然現れた
($mpc | select -index 0).headers.key[2]     # Content-Disposition
($mpc | select -index 0).headers.value[0]     # text/plain; charset=utf-8
($mpc | select -index 0).headers.value[1]     # 9
($mpc | select -index 0).headers.value[2]     # form-data; name=TestHeader   <- TestValue はどこ？
($mpc | select -index 1).headers
#>

Invoke-WebRequest -Uri $uri -body $mpc -Method 'POST' -ContentType $mpc.Headers.value
# $mpcが展開されない クラス名が出力される
# "System.Net.Http.StringContent System.Net.Http.StringContent"

<#
Invoke-WebRequest 
[-Uri] <uri> 
[-UseBasicParsing] 
[-WebSession <WebRequestSession>] 
[-SessionVariable <string>] 
[-Credential <pscredential>] 
[-UseDefaultCredentials] 
[-CertificateThumbprint <string>] 
[-Certificate <X509Certificate>] 
[-UserAgent <string>] 
[-DisableKeepAlive] 
[-TimeoutSec <int>] 
[-Headers <IDictionary>] 
[-MaximumRedirection <int>] 
[-Method <WebRequestMethod>] 
[-Proxy <uri>] 
[-ProxyCredential <pscredential>] 
[-ProxyUseDefaultCredentials] 
[-Body <Object>] 
[-ContentType <string>] 
[-TransferEncoding <string>] 
[-InFile <string>] 
[-OutFile <string>] 
[-PassThru] [<CommonParameters>]
#>