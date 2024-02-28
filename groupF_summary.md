Types of diagnoses and how they relate

“After viewing the description for the given dataset, we can be sure that we are presented with skin lesions such as: Basal Cell Carcinoma (BCC), Squamous Cell Carcinoma (SCC), Actinic Keratosis (ACK), Seborrheic Keratosis (SEK), Bowen’s disease (BOD), Melanoma (MEL), and Nevus (NEV).  These skin lesions are also divided into two groups: skin cancers (BCC, MEL, SCC(including BOD)), skin diseases (ACK, SEK, and NEV).  In addition, we may note that MEL, NEV, and SEK are pigmented skin lesions and SCC, BCC and ACK are non-pigmented ones.”1

BCC also known as Basal Cell Carcinoma, is a skin cancer type, which is one of the most common ones among different skin cancer types. In the data set there are a total of 845 instances of the BCC diagnoses, making it the most common one in the dataset.2 It generally contains features like bleeding, pain and present elevation. Features that are shared by the SCC skin cancer type, making it difficult to distinguish the two types based on those features.3

Missing data and low quality images.

Since there is a lot of missing data in the table provided to us, we were forced to clean it up.
When cleaning the data based on the columns “gender information”, “skin cancer history”, “cancer history”, 
“region”, “diagnostic” and “image id” we got a total of 804 rows where one of the before mentioned columns has NaN as its input.

No column in the data set shows whether or not the picture is of low quality, so there might be some pictures we can't use but since that data set after cleaning is 1494 
and that is too many pictures to go through one by one. Working with the data set description, we can be sure that the pictures are of different sizes and most likely of different quality, since they were made by different devices. Low-quality photos can affect masks, and accordingly they can affect the result of our research.

Prevalence of the different skin cancers and diseases:

For this part we have used our cleaned version of the dataset (Without all the null values)

We have 741 Males and 753 Females in the study, so 1494 people in total.

We can from our data deepdive see the following split between genders:

BCC: Males 439 (59.23%), Females 406 (53.91%), Both genders 845 (56.55%)

ACK: Males 130 (17.54%), Females 153 (20.31%), Both genders 283 (18.94%)

SCC: Males 102 (13.76%), Females 90  (11.95%), Both genders 192 (12.85%)

NEV: Males 26  ( 3.50%), Females 49  ( 6.50%), Both genders 75  ( 5.02%)

MEL: Males 24  ( 3.23%), Females 28  ( 3.71%), Both genders 52  ( 3.48%)

SEK: Males 20  ( 2.69%), Females 27  ( 3.58%), Both genders 47  ( 3.14%)

From these statistics we can see a significant difference in the prevalence of Nevus, there are almost 2 females with the skin disease for 1 man with the skin disease. 
This might indicate some sort of weakness for this specific disease in Females. 
There is also a difference in Actinic Keratosis for males and females, here there is 17.54% prevalence for males and 20.31% prevalence for females. 
There is a difference in the prevalence of Basal Cell Carcinoma, here the prevalence for males is 59.23% while it is 56.55% for females. 
Finally for Seborrheic Keratosis the difference in prevalence is  2.69% for males and 3.58% for females, which is a quite big difference.

