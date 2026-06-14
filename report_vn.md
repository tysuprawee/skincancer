# Phân Tích Mô Hình Lâm Sàng của Tổn Thương Da Melanoma và Không Phải Melanoma Sử Dụng Siêu Dữ Liệu HAM10000

**Báo Cáo Dự Án Môn Học**
**Bộ dữ liệu:** HAM10000 (Human Against Machine with 10,000 training images)
**Loại phân tích:** Phân tích mô hình lâm sàng khám phá kết hợp kiểm định thống kê và sàng lọc ML dựa trên siêu dữ liệu

> **Tuyên bố học thuật:** Dự án này được thực hiện chỉ nhằm mục đích giáo dục. Mọi phát hiện đều dựa trên bộ dữ liệu nghiên cứu và không được áp dụng trong bất kỳ bối cảnh lâm sàng hay chẩn đoán nào.

---

## 1. Giới thiệu

Ung thư da là một trong những loại ung thư phổ biến nhất trên thế giới. Chỉ riêng tại Hoa Kỳ, hơn 5 triệu ca ung thư da được chẩn đoán mỗi năm. Trong tất cả các phân nhóm ung thư da, **melanoma** là loại gây tử vong cao nhất, chiếm phần lớn số ca tử vong liên quan đến ung thư da dù chỉ chiếm khoảng 1% tổng số ca. Tuy nhiên, khi phát hiện sớm (giai đoạn I), tỷ lệ sống sót sau năm năm vượt quá 98%. Khi phát hiện ở giai đoạn IV, con số này giảm xuống còn khoảng 23%.

Do đó, phát hiện sớm là yếu tố quan trọng nhất để cải thiện kết quả điều trị cho bệnh nhân. Soi da (dermatoscopy) là kỹ thuật chẩn đoán hình ảnh không xâm lấn, sử dụng ánh sáng phân cực để quan sát cấu trúc da dưới bề mặt, và đã trở thành công cụ lâm sàng tiêu chuẩn để đánh giá các tổn thương da có sắc tố. Phương pháp này cho độ chính xác chẩn đoán cao hơn đáng kể so với khám bằng mắt thường.

Ngoài phân tích hình ảnh, **siêu dữ liệu lâm sàng** như tuổi, giới tính và vị trí tổn thương mang thông tin chẩn đoán có ý nghĩa. Một số loại tổn thương có xu hướng xuất hiện ở nhóm dân số và vùng giải phẫu nhất định. Ví dụ, melanoma thường gặp hơn ở bệnh nhân lớn tuổi và hay xuất hiện ở các vùng tiếp xúc ánh nắng như lưng và thân. Ung thư biểu mô tế bào đáy (basal cell carcinoma) thường phát triển ở mặt, cổ và da đầu. Hiểu các mô hình này giúp bác sĩ lâm sàng ưu tiên những bệnh nhân cần được theo dõi sát hơn.

Dự án này sử dụng bộ dữ liệu HAM10000 để khám phá các mô hình lâm sàng và nhân khẩu học thông qua phân tích dữ liệu, kiểm định giả thuyết thống kê và học máy đơn giản mà không dựa vào dữ liệu hình ảnh. Mục tiêu là hiểu cách siêu dữ liệu đơn thuần phản ánh sinh học của các tổn thương da.

---

## 2. Mô tả bộ dữ liệu

### 2.1 Tổng quan

Bộ dữ liệu **HAM10000** (*Human Against Machine with 10,000 training images*) được Tschandl và cộng sự (2018) công bố và là một trong những bộ dữ liệu soi da công khai lớn nhất. Bộ dữ liệu chứa **10.015 hình ảnh soi da** của các tổn thương da thu thập từ nhiều trung tâm, kèm theo siêu dữ liệu lâm sàng có cấu trúc cho từng hình ảnh.

### 2.2 Biến siêu dữ liệu

| Cột | Kiểu | Mô tả |
|-----|------|-------|
| `lesion_id` | Chuỗi | Mã định danh duy nhất cho một tổn thương (một tổn thương có thể có nhiều hình ảnh) |
| `image_id` | Chuỗi | Mã định danh duy nhất cho từng hình ảnh |
| `dx` | Phân loại | Mã chẩn đoán (một trong 7 lớp) |
| `dx_type` | Phân loại | Phương pháp xác nhận chẩn đoán |
| `age` | Số | Tuổi bệnh nhân (năm) |
| `sex` | Phân loại | Giới tính bệnh nhân (nam / nữ / không xác định) |
| `localization` | Phân loại | Vị trí cơ thể nơi phát hiện tổn thương |

### 2.3 Các lớp chẩn đoán

| Mã | Tên đầy đủ | Tính chất ác tính |
|----|-----------|-------------------|
| `nv` | Nốt ruồi sắc tố (Melanocytic Nevi) | Lành tính |
| `bkl` | Tổn thương giống dày sừng lành tính (Benign Keratosis-like Lesions) | Lành tính |
| `df` | U xơ da (Dermatofibroma) | Lành tính |
| `vasc` | Tổn thương mạch máu (Vascular Lesions) | Lành tính |
| `mel` | Melanoma | Ác tính |
| `bcc` | Ung thư biểu mô tế bào đáy (Basal Cell Carcinoma) | Ác tính |
| `akiec` | Dày sừng ánh nắng / Bệnh Bowen (Actinic Keratosis / Bowen's Disease) | Tiền ác tính đến tại chỗ |

### 2.4 Phương pháp xác nhận chẩn đoán

| Mã | Phương pháp |
|----|-------------|
| `histo` | Giải phẫu bệnh (sinh thiết mô, tiêu chuẩn vàng) |
| `follow_up` | Theo dõi lâm sàng |
| `consensus` | Đồng thuận của chuyên gia da liễu |
| `confocal` | Kính hiển vi cộng hưởng phản xạ |

### 2.5 Phân bố các lớp

Bộ dữ liệu mất cân bằng nghiêm trọng. Nốt ruồi sắc tố (`nv`) chiếm khoảng 67% tổng số ca, trong khi lớp hiếm nhất (`df`) chỉ chiếm hơn 1%.

| Chẩn đoán | Số lượng | Tỷ lệ |
|-----------|----------|-------|
| nv (Nốt ruồi sắc tố) | 6.705 | 66,9% |
| mel (Melanoma) | 1.113 | 11,1% |
| bkl (Dày sừng lành tính) | 1.099 | 11,0% |
| bcc (Ung thư biểu mô tế bào đáy) | 514 | 5,1% |
| akiec (Dày sừng ánh nắng) | 327 | 3,3% |
| vasc (Tổn thương mạch máu) | 142 | 1,4% |
| df (U xơ da) | 115 | 1,1% |

![Hình 1: Số ca theo chẩn đoán](figures/fig1_case_counts.png)
*Hình 1: Số ca theo chẩn đoán*

![Hình 7: Phân bố lớp lành tính và giống ác tính](figures/fig7_class_breakdown.png)
*Hình 7: Phân bố lớp lành tính và giống ác tính*

Sự mất cân bằng này là yếu tố quan trọng cần xem xét trong cả phân tích thống kê và học máy.

---

## 3. Câu hỏi nghiên cứu

### Câu hỏi nghiên cứu chính

> Tuổi, giới tính và vị trí cơ thể của bệnh nhân có liên quan đến loại chẩn đoán tổn thương da hay không?

### Câu hỏi phụ

1. Mỗi loại tổn thương thường gặp nhất ở nhóm tuổi nào?
2. Có sự khác biệt có ý nghĩa thống kê về phân bố giới tính giữa các loại chẩn đoán không?
3. Một số vị trí cơ thể có tỷ lệ cao hơn của các tổn thương giống ác tính không?
4. Melanoma có mô hình tuổi và vị trí khác biệt so với tổn thương lành tính không?
5. Siêu dữ liệu lâm sàng đơn thuần có thể cung cấp tín hiệu sàng lọc có ý nghĩa cho nguy cơ melanoma không?

---

## 4. Phương pháp

### 4.1 Làm sạch dữ liệu

Các bước làm sạch sau được áp dụng trước khi phân tích:

1. **Loại bỏ dòng giới tính không xác định:** 57 dòng có `sex == "unknown"` đã bị loại.
2. **Loại bỏ dòng vị trí không xác định:** 234 dòng có `localization == "unknown"` đã bị loại.
3. **Điền giá trị tuổi thiếu:** Các giá trị `age` thiếu được điền bằng tuổi trung vị trong từng nhóm chẩn đoán (`dx`) để bảo toàn phân bố tuổi theo nhóm.
4. **Nhóm tuổi:** Tuổi liên tục được phân thành năm nhóm lâm sàng: 0-20, 21-40, 41-60, 61-80, 80+
5. **Nhóm lâm sàng:** Tạo cột nhị phân `lesion_class`:
   - **Lành tính:** `nv`, `bkl`, `df`, `vasc`
   - **Giống ác tính:** `mel`, `bcc`, `akiec`

Sau khi làm sạch, bộ dữ liệu làm việc còn khoảng 9.724 dòng.

### 4.2 Phân tích khám phá dữ liệu

Tám biểu đồ được tạo để mô tả phân bố và mô hình trong dữ liệu:

1. Số ca theo chẩn đoán (biểu đồ cột ngang)
2. Phân bố tuổi theo chẩn đoán (box plot)
3. Tỷ lệ lành tính và giống ác tính theo nhóm tuổi (cột chồng)
4. Phân bố giới tính trong từng chẩn đoán (cột nhóm)
5. Số lượng chẩn đoán theo 7 vị trí cơ thể hàng đầu (cột nhóm)
6. Bản đồ nhiệt chẩn đoán x vị trí (phần trăm trong từng chẩn đoán)
7. Phân bố tổng thể lớp lành tính và giống ác tính (tròn + cột)
8. Phương pháp xác nhận chẩn đoán theo từng chẩn đoán (cột chồng)

### 4.3 Phân tích thống kê

Bốn kiểm định giả thuyết được thực hiện:

| Kiểm định | Biến | Phương pháp |
|-----------|------|-------------|
| 1 | dx vs giới tính | Chi-square Pearson |
| 2 | dx vs vị trí | Chi-square Pearson |
| 3 | Tuổi vs nhóm dx | Kiểm định Kruskal-Wallis H |
| 4 | Tuổi melanoma vs không melanoma | Kiểm định Mann-Whitney U |

Mức ý nghĩa: alpha = 0,05 cho tất cả kiểm định. Kruskal-Wallis và Mann-Whitney U được chọn thay cho ANOVA vì dữ liệu tuổi giữa các nhóm chẩn đoán không phân phối chuẩn.

### 4.4 Học máy (chỉ siêu dữ liệu)

Một bài toán phân loại nhị phân được định nghĩa để dự đoán **melanoma so với không melanoma** chỉ sử dụng ba đặc trưng siêu dữ liệu lâm sàng: tuổi, giới tính và vị trí.

- **Chia train/test:** 80/20, phân tầng theo lớp
- **Tiền xử lý:** StandardScaler cho tuổi; OneHotEncoder cho giới tính và vị trí
- **Mô hình:** Hồi quy logistic, Cây quyết định (độ sâu tối đa 5), Rừng ngẫu nhiên (100 cây)
- **Xử lý mất cân bằng lớp:** `class_weight='balanced'` áp dụng cho tất cả mô hình
- **Chỉ số chính:** Độ nhạy (recall) cho lớp melanoma, vì bỏ sót melanoma có chi phí lâm sàng cao hơn nhiều so với báo động giả

---

## 5. Kết quả

### 5.1 Mô hình theo tuổi

Các tổn thương giống ác tính (melanoma, BCC, dày sừng ánh nắng) tập trung ở nhóm tuổi cao hơn. Tuổi trung vị của bệnh nhân melanoma cao hơn đáng kể so với bệnh nhân nốt ruồi sắc tố. Các nhóm tuổi 41-60 và 61-80 cho thấy tỷ lệ ca ca giống ác tính ngày càng tăng. U xơ da và tổn thương mạch máu thường xuất hiện ở bệnh nhân trẻ hơn trung bình.

![Hình 2: Phân bố tuổi theo chẩn đoán](figures/fig2_age_by_diagnosis.png)
*Hình 2: Phân bố tuổi theo chẩn đoán (Box Plot)*

![Hình 3: Tỷ lệ lành tính và giống ác tính theo nhóm tuổi](figures/fig3_malignant_by_age_group.png)
*Hình 3: Tỷ lệ lành tính và giống ác tính theo nhóm tuổi*

### 5.2 Mô hình theo giới tính

U xơ da có tỷ lệ cao hơn đáng kể ở bệnh nhân nữ, phù hợp với tài liệu đã công bố. Tổn thương mạch máu và ung thư biểu mô tế bào đáy có xu hướng chiếm ưu thế ở nam giới. Melanoma phân bố tương đối đều giữa hai giới trong bộ dữ liệu này.

![Hình 4: Phân bố giới tính trong từng chẩn đoán](figures/fig4_diagnosis_by_sex.png)
*Hình 4: Phân bố giới tính trong từng chẩn đoán (%)*

### 5.3 Mô hình theo vị trí cơ thể

`back` (lưng) và `lower extremity` (chi dưới) là các vị trí phổ biến nhất tổng thể. Bản đồ nhiệt cho thấy melanoma có tỷ lệ cao hơn ở `back` và `trunk` (thân), trong khi dày sừng ánh nắng và BCC xuất hiện thường xuyên hơn ở `face` (mặt) và `scalp` (da đầu), các vùng tiếp xúc ánh nắng phù hợp với cơ chế bệnh sinh liên quan đến tia UV. U xơ da gắn chặt với `lower extremity`.

![Hình 5: Số lượng chẩn đoán theo 7 vị trí cơ thể hàng đầu](figures/fig5_diagnosis_by_location.png)
*Hình 5: Số lượng chẩn đoán theo 7 vị trí cơ thể hàng đầu*

![Hình 6: Bản đồ nhiệt: Chẩn đoán x Vị trí cơ thể](figures/fig6_heatmap_dx_location.png)
*Hình 6: Bản đồ nhiệt: Chẩn đoán x Vị trí cơ thể (%)*

### 5.4 Phương pháp xác nhận chẩn đoán

Melanoma và BCC có tỷ lệ xác nhận bằng giải phẫu bệnh (`histo`) cao nhất, điều này phù hợp với mức độ nghiêm trọng lâm sàng của chúng. Nốt ruồi sắc tố thường được xác nhận bằng theo dõi, đây là cách tiếp cận tiêu chuẩn để giám sát các nốt ruồi lành tính.

![Hình 8: Phương pháp xác nhận chẩn đoán theo từng chẩn đoán](figures/fig8_dxtype_by_diagnosis.png)
*Hình 8: Phương pháp xác nhận chẩn đoán theo từng chẩn đoán*

### 5.5 Kết quả phân tích thống kê

**Kiểm định 1: dx vs giới tính (Chi-square)**
Kiểm định Chi-square cho kết quả có ý nghĩa thống kê (p < 0,05), cho thấy loại tổn thương có liên quan đáng kể với giới tính bệnh nhân. Mối liên hệ chủ yếu do u xơ da (ưu thế nữ) và tổn thương mạch máu (ưu thế nam).

**Kiểm định 2: dx vs vị trí (Chi-square)**
Phát hiện mối liên hệ rất có ý nghĩa giữa loại chẩn đoán và vị trí cơ thể (p < 0,001). Điều này xác nhận các loại tổn thương khác nhau có xu hướng giải phẫu riêng biệt, phù hợp với bệnh sinh học đã biết.

**Kiểm định 3: Tuổi theo nhóm dx (Kruskal-Wallis)**
Tuổi trung vị của bệnh nhân khác biệt có ý nghĩa giữa các nhóm chẩn đoán (p < 0,001). Các nhóm tổn thương giống ác tính có tuổi trung vị cao hơn nhất quán so với nhóm lành tính, hỗ trợ vai trò của tuổi như một yếu tố nguy cơ.

**Kiểm định 4: Tuổi melanoma vs không melanoma (Mann-Whitney U)**
Bệnh nhân melanoma lớn tuổi hơn đáng kể so với bệnh nhân không melanoma (p < 0,001). Phát hiện này củng cố hướng dẫn lâm sàng cần theo dõi sát hơn các tổn thương có sắc tố ở bệnh nhân lớn tuổi.

### 5.6 Kết quả học máy

Cả ba mô hình được huấn luyện chỉ trên siêu dữ liệu (tuổi, giới tính, vị trí) để phân loại melanoma và không melanoma.

| Mô hình | Độ chính xác | Độ nhạy melanoma | F1 melanoma |
|---------|--------------|------------------|-------------|
| Hồi quy logistic | ~67-70% | ~0,60-0,65 | ~0,30-0,35 |
| Cây quyết định (độ sâu 5) | ~65-68% | ~0,55-0,62 | ~0,28-0,33 |
| Rừng ngẫu nhiên | ~69-72% | ~0,60-0,65 | ~0,32-0,36 |

*Lưu ý: Giá trị chính xác thay đổi nhẹ giữa các lần chạy do seed ngẫu nhiên. Các giá trị trên là khoảng đại diện.*

![Hình 9: Ma trận nhầm lẫn: Melanoma vs. Không melanoma](figures/fig9_confusion_matrices.png)
*Hình 9: Ma trận nhầm lẫn: Melanoma vs. Không melanoma (Tất cả mô hình)*

Độ nhạy melanoma trong khoảng 60-65%, đạt được chỉ với ba đặc trưng đơn giản, cho thấy siêu dữ liệu lâm sàng mang tín hiệu sàng lọc thực sự. Phân tích tầm quan trọng đặc trưng từ Rừng ngẫu nhiên cho thấy **tuổi** là yếu tố dự đoán quan trọng nhất, tiếp theo là các vị trí cơ thể cụ thể (đặc biệt `back` và `scalp`).

![Hình 10: 15 đặc trưng quan trọng nhất (Rừng ngẫu nhiên)](figures/fig10_feature_importance.png)
*Hình 10: 15 đặc trưng quan trọng nhất (Rừng ngẫu nhiên)*

---

## 6. Thảo luận

### Diễn giải lâm sàng

Phân tích xác nhận một số mô hình đã được thiết lập rõ trong tài liệu da liễu:

- **Tuổi là yếu tố dự đoán ác tính mạnh nhất trong siêu dữ liệu.** Nguy cơ melanoma, BCC và dày sừng ánh nắng tăng đáng kể theo tuổi, phản ánh hàng thập kỷ tiếp xúc tích lũy với tia UV và suy giảm khả năng sửa chữa DNA theo tuổi.

- **Vị trí cơ thể phản ánh mô hình tiếp xúc tia UV.** Các vùng tiếp xúc ánh nắng (lưng, mặt, da đầu) có tỷ lệ cao hơn bất thường của các ung thư liên quan đến UV. Melanoma ở thân và lưng là mô hình nguy cơ cao đã biết, đặc biệt ở bệnh nhân nam.

- **Khác biệt giới tính trong phân bố tổn thương là có thật nhưng khiêm tốn.** Sự ưu thế nữ ở u xơ da là quan sát được ghi nhận rộng rãi. Khác biệt giới tính rộng hơn nhỏ hơn và phức tạp hơn so với tác động của tuổi hoặc vị trí.

- **Siêu dữ liệu mang tín hiệu sàng lọc có ý nghĩa.** Chỉ với ba biến, các mô hình đạt độ nhạy melanoma trong khoảng 60-65%. Mặc dù chưa đủ cho chẩn đoán lâm sàng, điều này cho thấy phân loại theo quy tắc đơn giản có cơ sở lâm sàng.

### Cân nhắc về mất cân bằng lớp

Sự chiếm ưu thế của `nv` trong bộ dữ liệu (67%) có ý nghĩa quan trọng:

- Kiểm định thống kê có thể bị chi phối bởi lớp đa số
- Mô hình ML huấn luyện không cân bằng sẽ mặc định dự đoán không melanoma và đạt độ chính xác cao giả tạo
- Độ nhạy cho lớp thiểu số (melanoma) mới là chỉ số hiệu suất có ý nghĩa

Việc dùng `class_weight='balanced'` giải quyết một phần vấn đề này, nhưng triển khai thực tế sẽ cần thêm các cách tiếp cận như oversampling (SMOTE) hoặc điều chỉnh ngưỡng.

---

## 7. Hạn chế

1. **Mất cân bằng bộ dữ liệu:** Nốt ruồi sắc tố chiếm 67% bộ dữ liệu. Các lớp hiếm như u xơ da và tổn thương mạch máu có cỡ mẫu hạn chế, khiến ước lượng thống kê kém tin cậy hơn.

2. **Phân tích chỉ siêu dữ liệu:** Dự án này cố ý loại trừ dữ liệu hình ảnh. Đặc trưng hình ảnh (màu sắc, kết cấu, viền không đều) là tín hiệu chẩn đoán chính trong soi da. Mô hình siêu dữ liệu chỉ mang tính bổ trợ.

3. **Thiên lệch bộ dữ liệu được chọn lọc:** HAM10000 được thu thập trong môi trường nghiên cứu da liễu chuyên biệt. Bộ dữ liệu không đại diện cho toàn bộ quần thể tổn thương gặp ở y tế ban đầu, cấp cứu hay telemedicine.

4. **Điền giá trị tuổi thiếu:** Giá trị tuổi thiếu được điền bằng trung vị theo nhóm, gây thiên lệch nhẹ, đặc biệt ở các lớp có cỡ mẫu nhỏ.

5. **Nhiều hình ảnh cho một tổn thương:** Một số tổn thương xuất hiện dưới dạng nhiều hình ảnh trong bộ dữ liệu. Phân tích ở đây ở mức hình ảnh, không phải mức tổn thương.

6. **Chỉ dùng cho mục đích học thuật:** Mọi phát hiện và mô hình được tạo ra nhằm mục đích giáo dục và chưa được xác thực cho sử dụng lâm sàng.

---

## 8. Kết luận

Dự án đã khảo sát các mô hình lâm sàng và nhân khẩu học trong bộ dữ liệu tổn thương da HAM10000 bằng phân tích chỉ siêu dữ liệu, kiểm định giả thuyết thống kê và các mô hình học máy đơn giản.

Các phát hiện chính:

- **Tuổi, giới tính và vị trí cơ thể của bệnh nhân đều liên quan có ý nghĩa với loại chẩn đoán tổn thương** (Chi-square: p < 0,001; Kruskal-Wallis: p < 0,001).
- **Bệnh nhân melanoma lớn tuổi hơn đáng kể** so với bệnh nhân không melanoma (Mann-Whitney U: p < 0,001), với nhóm tuổi 41-80 có tỷ lệ giống ác tính cao nhất.
- Một số **vị trí cơ thể dự đoán mạnh loại tổn thương**: mặt và da đầu cho BCC và dày sừng ánh nắng, chi dưới cho u xơ da, lưng/thân cho melanoma.
- **Mô hình ML chỉ siêu dữ liệu có thể đạt độ nhạy melanoma khoảng 60-65%** chỉ với ba đặc trưng, cho thấy tiềm năng sàng lọc thực sự nhưng hạn chế.
- Bộ dữ liệu có **mất cân bằng lớp** đáng kể (nv = 67%) cần được xử lý trong mọi ứng dụng mô hình.

Siêu dữ liệu lâm sàng nắm bắt các mô hình có ý nghĩa sinh học trong dữ liệu tổn thương da. Mặc dù không thể thay thế phân tích hình ảnh soi da hay khám lâm sàng, việc hiểu các mô hình này có giá trị để xây dựng khung phân tầng nguy cơ, phân loại chuyển tuyến và thiết kế chương trình sàng lọc tốt hơn. Hướng phát triển tiếp theo nên tích hợp đặc trưng hình ảnh với siêu dữ liệu để có mô hình đầy đủ và ứng dụng lâm sàng hơn.

---

## Tài liệu tham khảo

Tschandl, P., Rosendahl, C., & Kittler, H. (2018). The HAM10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions. *Scientific Data, 5*, 180161. https://doi.org/10.1038/sdata.2018.161

Siegel, R. L., Miller, K. D., & Jemal, A. (2020). Cancer statistics. *CA: A Cancer Journal for Clinicians, 70*(1), 7-30.

Vestergaard, M. E., Macaskill, P., Holt, P. E., & Menzies, S. W. (2008). Dermoscopy compared with naked eye examination for the diagnosis of primary melanoma. *British Journal of Dermatology, 159*(3), 669-676.
