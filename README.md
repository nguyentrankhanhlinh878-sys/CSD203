# SMART ELEVATOR DISPATCH SIMULATOR
## Báo Cáo Kỹ Thuật & Tài Liệu Đặc Tả Toàn Diện Dự Án
### Đề Tài 9 — Môn Cấu Trúc Dữ Liệu và Giải Thuật (CSD203 — FA26)

---

> **THÔNG TIN DỰ ÁN & HỒ SƠ NHÓM:**
> - **Cơ sở đào tạo:** Trường Đại học FPT (FPT University)
> - **Môn học:** CSD203 — Data Structures and Algorithms (Ngôn ngữ: Python 3.12)
> - **Học kỳ:** Fall 2026 (FA26)
> - **Nhóm thực hiện (Group):** **LHX**
> - **Thành viên nhóm:**
>   1. **Nguyễn Trần Khánh Linh** — MSSV: **SE210467**
>   2. **Nguyễn Minh Hùng** — MSSV: **SE202011**
>   3. **Trương Lập Xuyên** — MSSV: **SE210486**
> - **Giảng viên hướng dẫn (Instructor):** Thầy **Huỳnh Ngọc Dũng**
> - **Tình trạng tài liệu:** Báo cáo kỹ thuật tổng hợp toàn diện (Hoàn thiện đồng bộ 4 Phases: Phase 1 $\rightarrow$ Phase 4)

---

## MỤC LỤC TỔNG QUAN

1. [TÓM TẮT DỰ ÁN (ABSTRACT) & TỪ KHÓA (KEYWORDS)](#tóm-tắt-dự-án-abstract--từ-khóa-keywords)
2. [I. GIỚI THIỆU & ĐẶT VẤN ĐỀ (INTRODUCTION)](#i-giới-thiệu--đặt-vấn-đề-introduction)
   - [A. Đặt vấn đề (Problem Statement)](#a-đặt-vấn-đề-problem-statement)
   - [B. Mục tiêu cụ thể (SMART Objectives)](#b-mục-tiêu-cụ-thể-smart-objectives)
   - [C. Phạm vi & Ràng buộc (Scope and Constraints)](#c-phạm-vi--ràng-buộc-scope-and-constraints)
3. [II. PHÂN RÃ BÀI TOÁN (PROBLEM DECOMPOSITION)](#ii-phân-rã-bài-toán-problem-decomposition)
   - [A. Cấu trúc phân rã hệ thống (System Breakdown)](#a-cấu-trúc-phân-rã-hệ-thống-system-breakdown)
   - [B. Bảng ma trận yêu cầu chức năng (Functional Requirements Matrix)](#b-bảng-ma-trận-yêu-cầu-chức-năng-functional-requirements-matrix)
4. [III. NHẬN DIỆN MẪU & LỰA CHỌN CẤU TRÚC DỮ LIỆU (PATTERN RECOGNITION)](#iii-nhận-diện-mẫu--lựa-chọn-cấu-trúc-dữ-liệu-pattern-recognition)
   - [A. Nhận diện đặc tính dữ liệu (Data Characteristics)](#a-nhận-diện-đặc-tính-dữ-liệu-data-characteristics)
   - [B. So sánh & Biện luận cấu trúc dữ liệu cốt lõi](#b-so-sánh--biện-luận-cấu-trúc-dữ-liệu-cốt-lõi)
5. [IV. THIẾT KẾ GIẢI PHÁP & TRỪU TƯỢNG HÓA DỮ LIỆU (SOLUTION DESIGN & ABSTRACTION)](#iv-thiết-kế-giải-pháp--trừu-tượng-hóa-dữ-liệu-solution-design--abstraction)
   - [A. Sơ đồ lớp chi tiết (UML Class Diagram)](#a-sơ-đồ-lớp-chi-tiết-uml-class-diagram)
   - [B. Đặc tả kiểu dữ liệu trừu tượng (ADT Formal Definitions)](#b-đặc-tả-kiểu-dữ-liệu-trừu-tượng-adt-formal-definitions)
   - [C. Bản đồ lưu trữ trạng thái lúc chạy (Runtime State & Storage Map)](#c-bản-đồ-lưu-trữ-trạng-thái-lúc-chạy-runtime-state--storage-map)
6. [V. THIẾT KẾ THUẬT TOÁN (ALGORITHM DESIGN)](#v-thiết-kế-thuật-toán-algorithm-design)
   - [A. Mã giả các thao tác cốt lõi (Pseudocode)](#a-mã-giả-các-thao-tác-cốt-lõi-pseudocode)
   - [B. Bảng chạy thử khô & Truy vết từng bước (Dry-run Trace)](#b-bảng-chạy-thử-khô--truy-vết-từng-bước-dry-run-trace)
7. [VI. ĐÁNH GIÁ GIẢI PHÁP & MÔ HÌNH HÓA UML (SOLUTION EVALUATION & UML)](#vi-đánh-giá-giải-pháp--mô-hình-hóa-uml-solution-evaluation--uml)
   - [A. Sơ đồ tuần tự & Sơ đồ trạng thái (UML Sequence & State Diagrams)](#a-sơ-đồ-tuần-tự--sơ-đồ-trạng-thái-uml-sequence--state-diagrams)
   - [B. Phân tích độ phức tạp thuật toán (Big-O Mathematical Analysis)](#b-phân-tích-độ-phức-tạp-thuật-toán-big-o-mathematical-analysis)
   - [C. Đo lường hiệu năng thực tế (Empirical Benchmarks)](#c-đo-lường-hiệu-năng-thực-tế-empirical-benchmarks)
8. [VII. CÀI ĐẶT THỰC NGHIỆM & TỐI ƯU HÓA (IMPLEMENTATION & OPTIMIZATION)](#vii-cài-đặt-thực-nghiệm--tối-ưu-hóa-implementation--optimization)
   - [A. Cấu trúc thư mục mã nguồn](#a-cấu-trúc-thư-mục-mã-nguồn)
   - [B. Các kỹ thuật tối ưu hóa chuyên sâu đã áp dụng](#b-các-kỹ-thuật-tối-ưu-hóa-chuyên-sâu-đã-áp-dụng)
   - [C. Kết quả kiểm thử tự động (Automated Unit Testing)](#c-kết-quả-kiểm-thử-tự-động-automated-unit-testing)
9. [VIII. NHẬT KÝ KIỂM TOÁN AI & PHÂN TÍCH LỖI (AI AUDIT & REFLECTION)](#viii-nhật-ký-kiểm-toán-ai--phân-tích-lỗi-ai-audit--reflection)
   - [A. Bảng tóm tắt Prompt cốt lõi qua các Phase](#a-bảng-tóm-tắt-prompt-cốt-lõi-qua-các-phase)
   - [B. Phân tích 2 lỗi logic nghiêm trọng phát hiện ở AI Output & Cách giải quyết](#b-phân-tích-2-lỗi-logic-nghiêm-trọng-phát-hiện-ở-ai-output--cách-giải-quyết)
   - [C. Tuyên bố làm chủ và quyết định thiết kế (Human Ownership Statement)](#c-tuyên-bố-làm-chủ-và-quyết-định-thiết-kế-human-ownership-statement)
10. [IX. ĐỐI CHIẾU KẾT QUẢ & ĐÁNH GIÁ (OUTCOMES VS. OBJECTIVES)](#ix-đối-chiếu-kết-quả--đánh-giá-outcomes-vs-objectives)
11. [X. KẾT LUẬN & HƯỚNG PHÁT TRIỂN (CONCLUSION & FUTURE WORK)](#x-kết-luận--hướng-phát-triển-conclusion--future-work)
12. [PHỤ LỤC (APPENDICES)](#phụ-lục-appendices)
    - [Phụ lục A: Bảng phân công đóng góp thành viên](#phụ-lục-a-bảng-phân-công-đóng-góp-thành-viên)
    - [Phụ lục B: Nhật ký thay đổi qua 4 Phase (Change Log)](#phụ-lục-b-nhật-ký-thay-đổi-qua-4-phase-change-log)
    - [Phụ lục C: Hướng dẫn sử dụng giao diện dòng lệnh (CLI User Manual)](#phụ-lục-c-hướng-dẫn-sử-dụng-giao-diện-dòng-lệnh-cli-user-manual)
    - [Phụ lục D: Cẩm nang đọc hiểu dành cho AI (AI Agent Interpretation Guide)](#phụ-lục-d-cẩm-nang-đọc-hiểu-dành-cho-ai-ai-agent-interpretation-guide)

---

## TÓM TẮT DỰ ÁN (ABSTRACT) & TỪ KHÓA (KEYWORDS)

### Tóm tắt tiếng Việt
Báo cáo trình bày thiết kế và cài đặt hoàn chỉnh hệ thống mô phỏng điều phối thang máy thông minh (**Smart Elevator Dispatch Simulator**) cho tòa nhà quy chuẩn 12 tầng gồm 10 cabin thang máy, thuộc khuôn khổ môn học Cấu trúc Dữ liệu và Giải thuật (CSD203, FA26). Dự án giải quyết thách thức tối ưu hóa tổ hợp trong Hệ thống Điều khiển Nhóm Thang máy (EGCS) thông qua mô hình lập lộ trình tĩnh theo lô (**Batch Route Planning**). Toàn bộ hệ thống được xây dựng trên ngôn ngữ Python 3.12 mà không sử dụng bất kỳ thư viện cấu trúc dữ liệu ngoài nào. 

Hệ thống kết hợp ba cấu trúc dữ liệu tự cài đặt: **FIFOQueue** với kỹ thuật nén mảng động để tiếp nhận các cuộc gọi từ sảnh tầng, **MinHeap** quản lý các tầng dừng theo chiều đi lên, và **MaxHeap** quản lý các tầng dừng theo chiều đi xuống. Quá trình điều phối được thực hiện qua hàm chi phí phân tầng (Tier-based Cost Function) với 3 cấp độ: đón tiện đường cùng chiều ($O(d)$), thang đứng yên ($O(d + 12)$), và thang ngược chiều/đã vượt qua ($O(d + 24)$). Lộ trình cuối cùng của mỗi thang máy được tổng hợp thông qua thuật toán quét hai chiều **LOOK**, đảm bảo loại trừ trùng lặp điểm dừng độc lập theo từng hàng đợi. Kết quả thực nghiệm qua 10 ca kiểm thử tự động chứng minh hệ thống đạt độ chính xác 100% về hướng phục vụ, thời gian thực thi thuật toán dưới 2 mili-giây, và kiểm soát tường minh trạng thái của tất cả 10 thang máy.

### Abstract in English
This report presents the design and implementation of an end-to-end Smart Elevator Dispatch Simulator for a 12-floor building with 10 elevator cabins, developed for the Data Structures and Algorithms course (CSD203, FA26). The project addresses combinatorial optimization challenges in Elevator Group Control Systems (EGCS) using a batch/static route planning model. Developed entirely in Python 3.12 with zero external libraries, the system features custom-built data structures: an array-compacted `FIFOQueue` for hall requests, a `MinHeap` for ascending stops, and a `MaxHeap` for descending stops. Dispatching is governed by a 3-tier heuristic cost function that prioritizes en-route pickups, penalizes idle activations, and defers opposite-direction assignments. Final routes are generated via the bidirectional LOOK algorithm with per-queue deduplication. Automated unit testing verifies 100% directional accuracy, sub-2ms batch processing latency, and explicit handling of both active and idle cabins.

### Từ khóa (Keywords)
- **Elevator Group Control System (EGCS)**
- **LOOK Algorithm / Elevator Scanning**
- **Dual Priority Queues (Min-Heap & Max-Heap)**
- **FIFO Queue with Array Compaction**
- **Tier-based Heuristic Cost Dispatching**
- **CSD203 FA26**

---

## I. GIỚI THIỆU & ĐẶT VẤN ĐỀ (INTRODUCTION)

### A. Đặt vấn đề (Problem Statement)
Trong các công trình cao tầng hiện đại, thang máy là huyết mạch giao thông trục đứng. Khi mật độ lưu thông tăng cao, phương pháp điều phối truyền thống (mỗi thang hoạt động độc lập hoặc chỉ phản ứng đơn lẻ với nút bấm gần nhất) dẫn tới nhiều hệ quả tiêu cực:
1. **Thời gian chờ đợi kéo dài (Prolonged Waiting Time):** Hành khách phải chờ thang di chuyển vòng vèo, dừng đỗ ngẫu nhiên không có trật tự.
2. **Hiện tượng chùm thang máy (Elevator Clustering):** Nhiều cabin cùng đổ dồn về một tầng để đón một vài hành khách, bỏ trống hoàn toàn các khu vực tầng khác của tòa nhà.
3. **Lãng phí năng lượng & Mài mòn cơ khí (Energy Inefficiency & Mechanical Wear):** Động cơ thang máy liên tục đảo chiều tăng giảm tốc đột ngột, dừng đón khách sai hướng làm tăng chu kỳ hành trình.
4. **Bỏ quên yêu cầu (Starvation):** Những hành khách ở các tầng biên hoặc bấm nút ngược với xu thế đám đông có thể bị bỏ qua trong thời gian dài.

Do đó, xây dựng một **Bộ điều phối nhóm thang máy (Group Dispatcher)** kết hợp thuật toán tối ưu hóa quỹ đạo là bài toán kinh điển, bắt buộc phải áp dụng các cấu trúc dữ liệu tiên tiến để xử lý đồng thời bài toán thời gian thực và chất lượng dịch vụ.

### B. Mục tiêu cụ thể (SMART Objectives)
Dự án đề ra 4 mục tiêu kỹ thuật cụ thể (Specific, Measurable, Achievable, Relevant, Time-bound):
- **Mục tiêu 1 (Tự chủ Cấu trúc Dữ liệu — 100% Zero-Dependency):** Tự lập trình thủ công hoàn toàn các lớp `MinHeap`, `MaxHeap`, và `FIFOQueue` từ nền tảng mảng động Python, tuyệt đối không dùng module `heapq`, `queue`, hay `collections.deque`.
- **Mục tiêu 2 (Thuật toán Điều phối Phân tầng Tối ưu):** Thiết kế và cài đặt hàm chi phí Heuristic 3 tầng ($\text{Tier 1, 2, 3}$) đánh giá toàn diện khoảng cách vật lý và quan hệ hướng chuyển động, đảm bảo phân bổ cuộc gọi sảnh đến thang máy có thời gian đón nhanh nhất.
- **Mục tiêu 3 (Lập Lộ trình LOOK 2 chiều Starvation-Free):** Áp dụng thuật toán quét LOOK trên cấu trúc Heap kép, đảm bảo toàn bộ hành khách bên trong cabin được đưa tới đúng tầng mong muốn và khách ngoài sảnh được đón đúng hướng di chuyển của họ.
- **Mục tiêu 4 (Giao diện Dòng lệnh Chuẩn hóa & Tin cậy):** Xây dựng CLI nhập liệu 3 bước siêu tốc, cơ chế kiểm duyệt dữ liệu đầu vào (Data Validation) nghiêm ngặt, xử lý tự động ký tự ẩn Unicode BOM, hiển thị đầy đủ nhật ký điều phối và phân định rõ ràng các thang hoạt động/đứng yên.

### C. Phạm vi & Ràng buộc (Scope and Constraints)

#### 1. Bảng phân định ranh giới (In-Scope vs. Out-of-Scope)

| Tiêu chí | Trong phạm vi (In-Scope — Có làm) | Ngoài phạm vi (Out-of-Scope — Không làm) |
|---|---|---|
| **Mô hình thời gian** | **Static Snapshot / Batch Processing**: Tiếp nhận toàn bộ trạng thái và yêu cầu tại thời điểm $t$, tính toán phân bổ và lập lộ trình một lần. | **Real-time Continuous Simulation**: Không tạo vòng lặp vô tận theo giây, không dùng `time.sleep()`, không mô phỏng luồng khách phát sinh động ngẫu nhiên. |
| **Quy mô hệ thống** | Cố định **12 tầng** (tầng 1 đến tầng 12) và **10 cabin thang máy** (ID 1 đến 10). | Không hỗ trợ số tầng động trong lúc chạy, không hỗ trợ tầng hầm ($< 1$) hay tầng lửng. |
| **Yêu cầu đầu vào** | Tiếp nhận đầy đủ 2 luồng: **External Requests** ($XU/XD$) và **Cabin Requests** ($E:Dest$). Hỗ trợ trạng thái ban đầu của thang gồm IDLE và MOVING. | Không hỗ trợ tính năng quẹt thẻ thang máy phân quyền, không hỗ trợ hủy yêu cầu (Cancel Request) sau khi đã nhập. |
| **Đặc tính vật lý** | Quãng đường tính theo số tầng chênh lệch ($|\text{floor}_1 - \text{floor}_2|$). Chi phí được định lượng bằng số tầng danh nghĩa. | Bỏ qua khối lượng tải trọng buồng thang (Weight Capacity), bỏ qua gia tốc cơ học, vận tốc động cơ và độ trễ đóng/mở cửa vật lý. |
| **Thuật toán cốt lõi** | Heuristic 3-Tier Greedy Dispatching kết hợp Bi-directional LOOK Algorithm trên Dual-Heap. | Không sử dụng mạng nơ-ron học tăng cường (RL), không sử dụng thuật toán di truyền (GA) hay tối ưu hóa bầy đàn (PSO). |

#### 2. Các giả định và bất biến của hệ thống (System Invariants)
- **Invariant 1 (Tầng hợp lệ):** Mọi chỉ số tầng $F$ trong hệ thống luôn thỏa mãn $1 \le F \le 12$ ($F \in \mathbb{Z}^+$).
- **Invariant 2 (Mã thang hợp lệ):** Mọi định danh thang máy $ID$ luôn thỏa mãn $1 \le ID \le 10$ ($ID \in \mathbb{Z}^+$).
- **Invariant 3 (Ràng buộc biên chiều gọi sảnh):** Tại tầng 1, người dùng không thể gọi nút $D$ (Down); tại tầng 12, người dùng không thể gọi nút $U$ (Up).
- **Invariant 4 (Cam kết hoàn thành hành trình):** Mọi cabin request đã được nạp vào thang máy chắc chắn sẽ được đưa vào lộ trình di chuyển cho tới khi rút cạn các Heap.

---

## II. PHÂN RÃ BÀI TOÁN (PROBLEM DECOMPOSITION)

### A. Cấu trúc phân rã hệ thống (System Breakdown)
Hệ thống được phân rã thành 5 module độc lập theo nguyên lý đơn nhiệm (Single Responsibility Principle - SRP):

```
                                  KIẾN TRÚC TỔNG THỂ HỆ THỐNG
                                
                  ┌──────────────────────────────────────────────┐
                  │              CLI Controller                  │
                  │   (Nhập liệu, Validation, Format Báo cáo)    │
                  └──────────────────────┬───────────────────────┘
                                         │ Chuyển đổi dữ liệu thô
                                         ▼
                  ┌──────────────────────────────────────────────┐
                  │                Domain Models                 │
                  │  (Elevator, Direction, State, Requests)      │
                  └──────────────┬────────────────┬──────────────┘
                                 │                │
            Quản lý hàng đợi gọi │                │ Quản lý điểm dừng LOOK
                                 ▼                ▼
                  ┌────────────────────┐   ┌─────────────────────┐
                  │     FIFOQueue      │   │ MinHeap  /  MaxHeap │
                  │  (Custom Module)   │   │   (Custom Module)   │
                  └──────────────┬─────┘   └──────────────┬──────┘
                                 │                        │
                                 └───────────┬────────────┘
                                             ▼
                  ┌──────────────────────────────────────────────┐
                  │               Group Dispatcher               │
                  │ (Hàm Cost 3 tầng, Lập lịch phân bổ & LOOK)   │
                  └──────────────────────────────────────────────┘
```

1. **Module 1 — Cấu trúc dữ liệu nền tảng (`src/data_structures.py`):**
   - Đảm nhiệm việc cài đặt mảng động Heap và Queue thủ công.
   - Chịu trách nhiệm bảo toàn cấu trúc cây nhị phân gần hoàn chỉnh của Heap và thứ tự FIFO của hàng đợi cuộc gọi sảnh.
2. **Module 2 — Mô hình nghiệp vụ thực thể (`src/models.py`):**
   - Định nghĩa các trạng thái thang (`ElevatorState`), hướng di chuyển (`Direction`), các loại request (`ExternalRequest`, `CabinRequest`).
   - Đóng gói thực thể `Elevator` chứa trạng thái nội tại, vị trí thực, đích đến ban đầu, và cặp cấu trúc `up_queue` (MinHeap), `down_queue` (MaxHeap).
3. **Module 3 — Lập lộ trình cục bộ LOOK (`Elevator.generate_route` trong `src/models.py`):**
   - Thuật toán quét LOOK cục bộ trong từng thang máy, tự động xác định chiều ưu tiên ban đầu đối với thang IDLE, quét tuần tự một chiều sau đó đảo chiều quét sạch các điểm dừng còn lại.
4. **Module 4 — Bộ điều phối nhóm trung tâm (`src/dispatcher.py`):**
   - Tiếp nhận hàng đợi FIFO các cuộc gọi sảnh và danh sách cuộc gọi buồng.
   - Tính toán hàm chi phí phân tầng (Tier 1/2/3) để gán việc cho thang máy có chi phí tối thiểu.
5. **Module 5 — Giao diện dòng lệnh & Điều khiển luồng (`src/main.py`):**
   - Quản trị tương tác người dùng qua 3 bước: Trạng thái 10 thang $\rightarrow$ Danh sách External Calls $\rightarrow$ Danh sách Cabin Calls.
   - Bắt lỗi biên tầng, kiểm duyệt regex cú pháp, tự động gán cấu hình mặc định (Auto-preset) khi nhấn Enter, và định dạng bảng kết quả cuối cùng.

### B. Bảng ma trận yêu cầu chức năng (Functional Requirements Matrix)

| Mã YC | Tên chức năng | Module đảm nhiệm | Mức độ ưu tiên | Mô tả chi tiết |
|---|---|---|:---:|---|
| **FR-01** | Khởi tạo trạng thái đa dạng 10 thang máy | `main.py`, `models.py` | **CAO** | Tiếp nhận chuỗi gồm 10 phần tử, hỗ trợ định dạng `<floor>` cho thang IDLE và `<floor>:<dest>` cho thang MOVING. Kiểm tra biên $1 \le \text{floor} \le 12$. |
| **FR-02** | Xử lý cuộc gọi trong cabin (Cabin Requests) | `models.py`, `dispatcher.py` | **CAO** | Nạp trực tiếp đích đến vào thang máy tương ứng với mức ưu tiên cao nhất trước khi phân bổ cuộc gọi sảnh. |
| **FR-03** | Điều phối cuộc gọi sảnh (External Requests) | `dispatcher.py`, `data_structures.py` | **CAO** | Hàng đợi `FIFOQueue` chứa các cuộc gọi sảnh. Lần lượt lấy ra và tìm thang máy có hàm chi phí `Cost` thấp nhất để phân bổ. |
| **FR-04** | Đánh giá chi phí phân tầng 3 cấp độ | `dispatcher.py` | **CAO** | Phân tầng rõ rệt: Tier 1 (Cùng chiều chưa qua: $d$), Tier 2 (Thang IDLE: $d + 12$), Tier 3 (Ngược chiều/đã qua: $d + 24$). |
| **FR-05** | Tạo lộ trình LOOK quét hai chiều | `models.py` | **CAO** | Sử dụng `MinHeap` rút trích điểm dừng tăng dần và `MaxHeap` rút trích điểm dừng giảm dần, loại bỏ các điểm dừng liền kề trùng nhau. |
| **FR-06** | Khử trùng lặp điểm dừng theo từng hàng đợi | `models.py` | **TRUNG BÌNH** | Cho phép cùng một tầng xuất hiện ở cả `up_queue` và `down_queue` nhưng không được trùng lặp trong cùng một chiều di chuyển. |
| **FR-07** | Hiển thị bảng tổng hợp và trạng thái IDLE | `main.py` | **TRUNG BÌNH** | Xuất nhật ký gán lệnh chi tiết, hiển thị tường minh lộ trình từng thang hoặc in rõ `IDLE (No movement)` nếu thang đứng yên. |

---

## III. NHẬN DIỆN MẪU & LỰA CHỌN CẤU TRÚC DỮ LIỆU (PATTERN RECOGNITION)

### A. Nhận diện đặc tính dữ liệu (Data Characteristics)
Khi phân tích luồng dữ liệu của hệ thống thang máy nhóm, nhóm tác giả nhận diện 4 đặc tính then chốt:
1. **Đặc tính FIFO của cuộc gọi sảnh:** Các hành khách đứng ngoài sảnh bấm nút theo thứ tự thời gian. Để đảm bảo công bằng và tránh starvation, các cuộc gọi cần được xử lý theo trật tự "ai đến trước được điều phối trước" (First-Come, First-Served).
2. **Đặc tính đơn điệu của quỹ đạo chuyển động (Directional Monotonicity):** 
   - Khi thang máy đi lên từ tầng 1 đến tầng 12, các điểm dừng **bắt buộc phải xuất hiện theo thứ tự tăng dần** ($3 \rightarrow 5 \rightarrow 8 \rightarrow 11$). Bất kỳ sự đảo lộn nào (như $3 \rightarrow 8 \rightarrow 5$) đều tạo ra chuyển động giật cục vô lý.
   - Ngược lại, khi thang đi xuống, các điểm dừng **bắt buộc phải xuất hiện theo thứ tự giảm dần** ($10 \rightarrow 7 \rightarrow 4 \rightarrow 1$).
3. **Đặc tính ưu tiên cục bộ (Priority of Proximity):** Điểm dừng tiếp theo của thang máy luôn là tầng gần vị trí hiện tại nhất theo hướng đang di chuyển.
4. **Đặc tính độc lập của 2 chiều quét (Bidirectional Independence):** Hành khách bấm gọi thang tại tầng 6 đi lên là yêu cầu tách biệt với hành khách tại tầng 6 đi xuống. Do đó, điểm dừng tầng 6 có thể xuất hiện độc lập ở cả 2 pha của lộ trình.

### B. So sánh & Biện luận cấu trúc dữ liệu cốt lõi

Nhóm tác giả đã tiến hành đối chiếu và đánh giá 4 phương án cấu trúc dữ liệu:

```
                            BẢNG SO SÁNH CÁC CẤU TRÚC DỮ LIỆU
┌───────────────────────┬──────────────┬──────────────┬────────────────────────────────────────────┐
│ Cấu trúc dữ liệu      │ Thao tác     │ Độ phức tạp  │ Nhận xét & Đánh giá ứng dụng               │
├───────────────────────┼──────────────┼──────────────┼────────────────────────────────────────────┤
│ Mảng tĩnh/Danh sách   │ Insert       │ O(1)         │ Chèn nhanh nhưng mỗi lần cần tìm tầng kế   │
│ không sắp xếp         │ Find Min/Max │ O(K)         │ tiếp phải quét toàn bộ danh sách. Không    │
│                       │ Delete       │ O(K)         │ đáp ứng tốt khi số lượng tầng dừng lớn.    │
├───────────────────────┼──────────────┼──────────────┼────────────────────────────────────────────┤
│ Danh sách liên kết    │ Insert (Sort)│ O(K)         │ Luôn giữ được thứ tự nhưng chi phí chèn    │
│ có thứ tự (Sorted LL) │ Extract Head │ O(1)         │ tuyến tính O(K) do phải duyệt tuần tự.     │
├───────────────────────┼──────────────┼──────────────┼────────────────────────────────────────────┤
│ Hàng đợi ưu tiên đơn  │ Insert       │ O(log K)     │ Tốt cho 1 chiều, nhưng khi thang cần đổi   │
│ (Single Priority Queue│ Extract      │ O(log K)     │ chiều thì cây Heap đơn không thể tự đảo    │
│                       │              │              │ thứ tự Min sang Max hiệu quả.              │
├───────────────────────┼──────────────┼──────────────┼────────────────────────────────────────────┤
│ **Heap Kép (Dual Heaps│ Insert       │ O(log K)     │ **LỰA CHỌN TỐI ƯU CỐT LÕI:** Tách biệt     │
│ MinHeap + MaxHeap)**  │ Extract      │ O(log K)     │ hoàn toàn chiều UP (MinHeap) và chiều DOWN │
│                       │ Peek         │ O(1)         │ (MaxHeap). Tạo lộ trình LOOK cực nhanh.    │
└───────────────────────┴──────────────┴──────────────┴────────────────────────────────────────────┘
```

#### Biện luận lựa chọn chính thức:
1. **Lựa chọn `FIFOQueue` cho Cuộc gọi sảnh:** Đảm bảo tính công bằng tuần tự. Sử dụng kỹ thuật con trỏ `_head` kết hợp dọn rác mảng (compaction) giúp thao tác `enqueue` và `dequeue` đều đạt $O(1)$.
2. **Lựa chọn `MinHeap` cho Lộ trình đi lên:** Gốc của Min-Heap luôn lưu trữ tầng nhỏ nhất trong các tầng cao hơn vị trí hiện tại. Thao tác lấy điểm dừng tiếp theo đạt $O(1)$ qua `peek()` và $O(\log K)$ khi rút trích qua `extract_min()`.
3. **Lựa chọn `MaxHeap` cho Lộ trình đi xuống:** Gốc của Max-Heap luôn lưu trữ tầng lớn nhất trong các tầng thấp hơn vị trí hiện tại. Rút trích theo trật tự giảm dần đạt $O(\log K)$ qua `extract_max()`.
4. **Chống trùng theo từng heap bằng `contains()`, kết hợp `Set` (`planned_stops`):** `add_stop` kiểm tra `up_queue.contains(floor)` hoặc `down_queue.contains(floor)` (duyệt $O(K)$, $K \le 12$) trước khi chèn, nên một tầng có thể nằm ở **cả hai** heap (đón UP và đón DOWN tại cùng tầng). `planned_stops` là tập hợp các tầng có trong lộ trình (hợp của 2 heap), chỉ dùng để kiểm tra thang có cần di chuyển hay không (`has_movement()`), **không** dùng để chống trùng (xem Mục VIII.B, Lỗi 2).

---

## IV. THIẾT KẾ GIẢI PHÁP & TRỪU TƯỢNG HÓA DỮ LIỆU (SOLUTION DESIGN & ABSTRACTION)

### A. Sơ đồ lớp chi tiết (UML Class Diagram)

```mermaid
classDiagram
    direction TB

    class Direction {
        <<enumeration>>
        UP
        DOWN
        NONE
        +__str__() str
    }

    class ElevatorState {
        <<enumeration>>
        IDLE
        MOVING_UP
        MOVING_DOWN
        +__str__() str
    }

    class ExternalRequest {
        +int floor
        +Direction direction
        +__repr__() str
    }

    class CabinRequest {
        +int elevator_id
        +int target_floor
        +__repr__() str
    }

    class MinHeap {
        -List~int~ _data
        +insert(val: int) void
        +extract_min() int
        +peek() int
        +is_empty() bool
        +contains(val: int) bool
        +__len__() int
        -_heapify_up(idx: int) void
        -_heapify_down(idx: int) void
    }

    class MaxHeap {
        -List~int~ _data
        +insert(val: int) void
        +extract_max() int
        +peek() int
        +is_empty() bool
        +contains(val: int) bool
        +__len__() int
        -_heapify_up(idx: int) void
        -_heapify_down(idx: int) void
    }

    class FIFOQueue {
        -List _items
        -int _head
        +enqueue(item: Any) void
        +dequeue() Any
        +peek() Any
        +is_empty() bool
        +__len__() int
    }

    class Elevator {
        +int id
        +int initial_floor
        +int current_floor
        +Optional~int~ initial_dest
        +ElevatorState state
        +MinHeap up_queue
        +MaxHeap down_queue
        +Set~int~ planned_stops
        +add_stop(floor: int, dir_intent: Direction) bool
        +has_movement() bool
        +generate_route() List~int~
    }

    class GroupDispatcher {
        +List~Elevator~ elevators
        +int total_floors
        +get_elevator(elevator_id: int) Elevator
        +calculate_cost(elevator: Elevator, req: ExternalRequest) int
        +dispatch_external(req: ExternalRequest) Tuple~Elevator, int~
        +process_cabin(req: CabinRequest) void
        +run_dispatch(external_queue: FIFOQueue, cabin_requests: List~CabinRequest~) List~str~
    }

    Elevator "1" *-- "1" MinHeap : up_queue
    Elevator "1" *-- "1" MaxHeap : down_queue
    Elevator o-- ElevatorState : state
    ExternalRequest o-- Direction : direction
    GroupDispatcher "1" o-- "10" Elevator : manages
    GroupDispatcher ..> FIFOQueue : consumes
    GroupDispatcher ..> ExternalRequest : dispatches
    GroupDispatcher ..> CabinRequest : dispatches
```

### B. Đặc tả kiểu dữ liệu trừu tượng (ADT Formal Definitions)

#### 1. ADT `MinHeap`
- **Mô tả trừu tượng:** Cấu trúc dữ liệu cây nhị phân lưu trữ tập hợp các số nguyên, duy trì tính chất nút cha luôn nhỏ hơn hoặc bằng các nút con.
- **Tập thao tác (Operations):**
  - $\text{Create}() \rightarrow \text{MinHeap}$: Khởi tạo một heap rỗng.
  - $\text{Insert}(v \in \mathbb{Z}^+)$: Thêm giá trị $v$ vào heap, bảo toàn tính chất Min-Heap sau $O(\log K)$ bước.
  - $\text{ExtractMin}() \rightarrow v \in \mathbb{Z}^+$: Xóa và trả về phần tử nhỏ nhất tại gốc, tái cân bằng cây trong $O(\log K)$ bước.
  - $\text{Peek}() \rightarrow v \in \mathbb{Z}^+$: Trả về phần tử nhỏ nhất mà không xóa, độ phức tạp $O(1)$.
  - $\text{Contains}(v \in \mathbb{Z}^+) \rightarrow \text{bool}$: Kiểm tra xem phần tử $v$ đã có trong heap hay chưa.
  - $\text{IsEmpty}() \rightarrow \text{bool}$: Kiểm tra heap có chứa phần tử nào không.

#### 2. ADT `MaxHeap`
- **Mô tả trừu tượng:** Cấu trúc dữ liệu cây nhị phân lưu trữ tập hợp các số nguyên, duy trì tính chất nút cha luôn lớn hơn hoặc bằng các nút con.
- **Tập thao tác (Operations):**
  - $\text{Create}() \rightarrow \text{MaxHeap}$: Khởi tạo một heap rỗng.
  - $\text{Insert}(v \in \mathbb{Z}^+)$: Thêm giá trị $v$ vào heap, bảo toàn tính chất Max-Heap sau $O(\log K)$ bước.
  - $\text{ExtractMax}() \rightarrow v \in \mathbb{Z}^+$: Xóa và trả về phần tử lớn nhất tại gốc, tái cân bằng cây trong $O(\log K)$ bước.
  - $\text{Peek}() \rightarrow v \in \mathbb{Z}^+$: Trả về phần tử lớn nhất mà không xóa, độ phức tạp $O(1)$.
  - $\text{Contains}(v \in \mathbb{Z}^+) \rightarrow \text{bool}$: Kiểm tra phần tử $v$ đã có trong heap hay chưa.
  - $\text{IsEmpty}() \rightarrow \text{bool}$: Kiểm tra heap rỗng.

#### 3. ADT `FIFOQueue`
- **Mô tả trừu tượng:** Danh sách tuyến tính hỗ trợ chèn phần tử ở đuôi và rút phần tử ở đầu theo nguyên lý First-In-First-Out.
- **Tập thao tác (Operations):**
  - $\text{Enqueue}(x)$: Đưa phần tử $x$ vào cuối hàng đợi.
  - $\text{Dequeue}() \rightarrow x$: Lấy và xóa phần tử ở đầu hàng đợi, tự động nén bộ nhớ nếu chỉ số trôi vượt ngưỡng.
  - $\text{Peek}() \rightarrow x$: Xem phần tử ở đầu hàng đợi.
  - $\text{IsEmpty}() \rightarrow \text{bool}$: Trả về true nếu hàng đợi không còn phần tử.

#### 4. ADT `Elevator`
- **Thuộc tính trạng thái:** $\text{ID} \in [1..10]$, $\text{CurrentFloor} \in [1..12]$, $\text{State} \in \{\text{IDLE}, \text{MOVING\_UP}, \text{MOVING\_DOWN}\}$.
- **Tập thao tác (Operations):**
  - $\text{AddStop}(\text{floor}, \text{dir\_intent}) \rightarrow \text{bool}$: Định tuyến tầng dừng vào `up_queue` hoặc `down_queue` dựa trên hướng dự định hoặc vị trí tương đối; kiểm tra chống trùng lặp theo từng queue.
  - $\text{GenerateRoute}() \rightarrow \text{List}[\mathbb{Z}^+]$: Thực thi thuật toán LOOK trên **bản sao** của 2 heap (heap gốc giữ nguyên), trả về danh sách lộ trình hoàn chỉnh.
  - $\text{HasMovement}() \rightarrow \text{bool}$: Trả về true nếu `planned_stops` khác rỗng.

### C. Bản đồ lưu trữ trạng thái lúc chạy (Runtime State & Storage Map)

> Bản đầy đủ (kèm trace từng giai đoạn với dữ liệu thật): [docs/STATE_AND_STORAGE.md](docs/STATE_AND_STORAGE.md)

| Dữ liệu | Lưu ở đâu | Cấu trúc | Vòng đời / Ai thay đổi |
|---|---|---|---|
| Trạng thái 10 thang | `elevators` (cục bộ trong `main`, dùng chung tham chiếu với `GroupDispatcher.elevators`) | `List[Elevator]` | Tạo ở Step 1; giữ giữa các lượt hoặc khởi tạo lại theo lựa chọn người dùng |
| `current_floor` | Thuộc tính `Elevator` | `int` | Cập nhật theo từng chặng; dùng làm vị trí bắt đầu của lượt kế tiếp |
| `state` | Thuộc tính `Elevator` | `ElevatorState` | `add_stop` đặt `IDLE → MOVING_*`; `finish_route` đặt lại `IDLE` sau khi phục vụ xong |
| Hall Request (trước gán) | `external_requests` → `up_external_queue` / `down_external_queue` | `List[ExternalRequest]` → 2 `FIFOQueue` (`_items` + `_head`, không có `_tail`) | Dequeue lần lượt: hết UP rồi tới DOWN |
| Hall Request (sau gán) | Heap của thang được chọn | `int` (chỉ số tầng). Hướng được mã hóa bằng việc tầng nằm ở `up_queue` hay `down_queue` | Object `ExternalRequest` không được giữ lại |
| Cabin Request | `cabin_requests` → heap của `elevators[id-1]` | `List[CabinRequest]` → `int` trong heap | Nạp **trước** Hall Request; heap chọn theo `target` so với `current_floor` |
| Điểm dừng | `up_queue._data`, `down_queue._data` | Mảng biểu diễn cây nhị phân hoàn chỉnh | Chỉ thêm, không bao giờ bị rút trên bản gốc |
| Chống trùng | `heap.contains()` theo **từng** heap | Duyệt tuyến tính O(k), k ≤ 12 | Cho phép một tầng nằm ở cả hai heap |
| `planned_stops` | Thuộc tính `Elevator` | `set[int]` (hợp của 2 heap) | **Chỉ** dùng cho `has_movement()`; không dùng để chống trùng |
| Lộ trình | Biến cục bộ `route` trong `generate_route` | `list[int]` | Tạo mới mỗi lần gọi từ `current_floor`, không lưu vào `Elevator` |
| Log | `logs` trong `run_dispatch` | `List[str]` | Cabin → External UP → External DOWN |

---

## V. THIẾT KẾ THUẬT TOÁN (ALGORITHM DESIGN)

### A. Mã giả các thao tác cốt lõi (Pseudocode)

#### 1. Thuật toán Vun đống trong MinHeap (`_heapify_up` & `_heapify_down`)
```text
ALGORITHM MinHeap_Insert(heap, value):
    heap._data.append(value)
    idx = length(heap._data) - 1
    parent = (idx - 1) // 2
    WHILE idx > 0 AND heap._data[idx] < heap._data[parent] DO:
        SWAP heap._data[idx] WITH heap._data[parent]
        idx = parent
        parent = (idx - 1) // 2
    END WHILE
END ALGORITHM

ALGORITHM MinHeap_ExtractMin(heap):
    IF heap is empty THEN ERROR "Empty Heap"
    min_val = heap._data[0]
    last_val = heap._data.pop()
    IF heap._data is not empty THEN:
        heap._data[0] = last_val
        idx = 0
        size = length(heap._data)
        LOOP FOREVER:
            smallest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2
            IF left < size AND heap._data[left] < heap._data[smallest] THEN:
                smallest = left
            IF right < size AND heap._data[right] < heap._data[smallest] THEN:
                smallest = right
            IF smallest != idx THEN:
                SWAP heap._data[idx] WITH heap._data[smallest]
                idx = smallest
            ELSE:
                BREAK
            END IF
        END LOOP
    END IF
    RETURN min_val
END ALGORITHM
```

#### 2. Thuật toán Hàm Chi Phí Điều Phối Phân Tầng (`calculate_cost`)
```text
ALGORITHM CalculateCost(elevator, request, total_floors = 12):
    dist = ABS(elevator.current_floor - request.floor)

    // TIER 1: Cùng chiều chuyển động và chưa chạy qua tầng gọi
    IF elevator.state == MOVING_UP AND request.direction == UP THEN:
        IF elevator.current_floor <= request.floor THEN:
            RETURN dist
        END IF
    ELSE IF elevator.state == MOVING_DOWN AND request.direction == DOWN THEN:
        IF elevator.current_floor >= request.floor THEN:
            RETURN dist
        END IF
    END IF

    // TIER 2: Thang máy đang đứng yên hoàn toàn
    IF elevator.state == IDLE THEN:
        RETURN dist + total_floors
    END IF

    // TIER 3: Ngược chiều di chuyển hoặc đã chạy vượt qua tầng gọi
    RETURN dist + (2 * total_floors)
END ALGORITHM
```

#### 3. Thuật toán Quy Trình Điều Phối Nhóm (`run_dispatch`)
```text
ALGORITHM RunDispatch(elevators, external_queue, cabin_requests):
    logs = Empty List

    // BƯỚC 1: Xử lý toàn bộ Cabin Requests trước (ưu tiên hành khách đã trong thang)
    FOR EACH cab_req IN cabin_requests DO:
        target_elevator = elevators[cab_req.elevator_id - 1]
        target_elevator.add_stop(cab_req.target_floor, Direction.NONE)
        logs.append("Cabin Request logged")
    END FOR

    // BƯỚC 2: Phục vụ tuần tự từng External Request trong FIFOQueue
    WHILE NOT external_queue.is_empty() DO:
        ext_req = external_queue.dequeue()
        best_elevator = NULL
        min_cost = INFINITY

        FOR EACH elev IN elevators DO:
            cost = CalculateCost(elev, ext_req)
            IF cost < min_cost THEN:
                min_cost = cost
                best_elevator = elev
            END IF
        END FOR

        best_elevator.add_stop(ext_req.floor, ext_req.direction)
        logs.append(FormatLog(ext_req, best_elevator.id, min_cost))
    END WHILE

    RETURN logs
END ALGORITHM
```

#### 4. Thuật toán Lập Lộ Trình LOOK Quét Hai Chiều (`generate_route`)
```text
ALGORITHM GenerateRoute(elevator):
    route = [elevator.current_floor]
    IF elevator has no movement THEN:
        RETURN route
    END IF

    primary_dir = elevator.state
    curr = elevator.current_floor

    // Nếu ban đầu thang đứng yên, chọn hướng có điểm dừng gần nhất
    IF primary_dir == IDLE THEN:
        IF NOT elevator.up_queue.is_empty() AND NOT elevator.down_queue.is_empty() THEN:
            dist_up = ABS(elevator.up_queue.peek() - curr)
            dist_down = ABS(elevator.down_queue.peek() - curr)
            IF dist_up <= dist_down THEN primary_dir = MOVING_UP ELSE primary_dir = MOVING_DOWN
        ELSE IF NOT elevator.up_queue.is_empty() THEN:
            primary_dir = MOVING_UP
        ELSE:
            primary_dir = MOVING_DOWN
        END IF
    END IF

    // Sao chép các Heap để không làm biến đổi dữ liệu nội tại (Non-destructive)
    up_copy = elevator.up_queue.copy()
    down_copy = elevator.down_queue.copy()
    up_stops = [up_copy.extract_min() while up_copy not empty]
    down_stops = [down_copy.extract_max() while down_copy not empty]

    // Quét LOOK đa pha đơn điệu (Phased Monotonic LOOK):
    IF primary_dir == MOVING_UP THEN:
        phase1 = [f IN up_stops WHERE f >= curr]      // Chiều lên phía trước
        phase2 = down_stops                           // Đảo chiều xuống
        phase3 = [f IN up_stops WHERE f < curr]       // Quét nốt chiều lên phía sau
        all_stops = phase1 + phase2 + phase3
    ELSE // MOVING_DOWN
        phase1 = [f IN down_stops WHERE f <= curr]    // Chiều xuống phía trước
        phase2 = up_stops                             // Đảo chiều lên
        phase3 = [f IN down_stops WHERE f > curr]     // Quét nốt chiều xuống phía sau
        all_stops = phase1 + phase2 + phase3
    END IF

    FOR EACH stop IN all_stops DO:
        IF stop != route.last() THEN route.append(stop)
    END FOR

    RETURN route
END ALGORITHM
```

### B. Bảng chạy thử khô & Truy vết từng bước (Dry-run Trace)

Giả sử hệ thống đang có cấu hình thu nhỏ gồm 3 thang máy tại tòa nhà 12 tầng:
- **E1**: Đang ở tầng 1, hướng đi lên tầng 12 (`1:12`, State: `MOVING_UP`).
- **E2**: Đang ở tầng 6, hướng đi xuống tầng 2 (`6:2`, State: `MOVING_DOWN`).
- **E3**: Đang ở tầng 4, đứng yên (`4`, State: `IDLE`).

Chuỗi yêu cầu ngoài sảnh trong `FIFOQueue`: `[5U, 3D, 8U]`.

#### Bảng vết tính toán hàm chi phí:

| Bước | Yêu cầu | Đánh giá E1 (1 $\uparrow$ 12) | Đánh giá E2 (6 $\downarrow$ 2) | Đánh giá E3 (4 IDLE) | Thang được chọn | Giải thích kết quả |
|:---:|:---:|---|---|---|:---:|---|
| **1** | **`5U`** | Tier 1: $5 - 1 = \mathbf{4}$ | Tier 3: $1 + 24 = 25$ | Tier 2: $1 + 12 = 13$ | **E1** (Cost: 4) | E1 đang đi lên từ 1, tầng 5 nằm trên lộ trình thẳng. |
| **2** | **`3D`** | Tier 3: $2 + 24 = 26$ | Tier 1: $6 - 3 = \mathbf{3}$ | Tier 2: $1 + 12 = 13$ | **E2** (Cost: 3) | E2 đang đi xuống từ 6, tầng 3 nằm tiện đường đón. |
| **3** | **`8U`** | Tier 1: $8 - 1 = \mathbf{7}$ | Tier 3: $2 + 24 = 26$ | Tier 2: $4 + 12 = 16$ | **E1** (Cost: 7) | E1 tiếp tục gom khách đi lên tầng 8. |

#### Trạng thái các Heap sau khi phân bổ:
- **E1**: `up_queue` (MinHeap) chứa: `[5, 8, 12]` $\rightarrow$ Lộ trình sinh ra: `1 -> 5 -> 8 -> 12`.
- **E2**: `down_queue` (MaxHeap) chứa: `[3, 2]` $\rightarrow$ Lộ trình sinh ra: `6 -> 3 -> 2`.
- **E3**: Cả 2 queue đều rỗng $\rightarrow$ Lộ trình: `IDLE (No movement)`.

---

## VI. ĐÁNH GIÁ GIẢI PHÁP & MÔ HÌNH HÓA UML (SOLUTION EVALUATION & UML)

### A. Sơ đồ tuần tự & Sơ đồ trạng thái (UML Sequence & State Diagrams)

#### 1. Sơ đồ tuần tự quy trình điều phối và xuất kết quả (Sequence Diagram)

```mermaid
sequenceDiagram
    autonumber
    actor User as Người dùng
    participant CLI as CLI Controller (main.py)
    participant Disp as GroupDispatcher
    participant Elev as Elevator (1..10)
    participant Q as FIFOQueue (Calls)
    participant Heap as MinHeap / MaxHeap

    User->>CLI: Nhập trạng thái 10 thang (E>)
    User->>CLI: Nhập External Requests (X>)
    User->>CLI: Nhập Cabin Requests (C>)

    Note over CLI,Disp: Giai đoạn 1: Nạp Cabin Requests
    loop Mỗi Cabin Request
        CLI->>Disp: process_cabin(cab_req)
        Disp->>Elev: add_stop(target_floor)
        Elev->>Heap: insert(target_floor)
    end

    Note over CLI,Q: Giai đoạn 2: Điều phối External Requests
    loop Cho đến khi FIFOQueue rỗng
        CLI->>Disp: run_dispatch()
        Disp->>Q: dequeue() -> ext_req
        loop 10 Thang máy
            Disp->>Disp: calculate_cost(elevator_i, ext_req)
        end
        Disp->>Elev: add_stop(req.floor, req.direction) cho Best Elevator
        Elev->>Heap: insert(req.floor) vào Heap tương ứng
    end

    Note over CLI,Elev: Giai đoạn 3: Tổng hợp Lộ trình LOOK
    loop 10 Thang máy
        CLI->>Elev: generate_route()
        Elev->>Heap: Rút sạch extract_min() & extract_max()
        Elev-->>CLI: Danh sách lộ trình [floor_1, floor_2, ...]
    end

    CLI-->>User: In bảng Final Elevator Routes & Trạng thái IDLE
```

#### 2. Sơ đồ máy trạng thái thang máy (State Machine Diagram)

**(a) Thuộc tính `Elevator.state` trong quá trình điều phối** (đúng theo `__init__` và `add_stop`):

```mermaid
stateDiagram-v2
    [*] --> IDLE : Khởi tạo với <floor>
    [*] --> MOVING_UP : Khởi tạo với <floor>:<dest> (dest > floor)
    [*] --> MOVING_DOWN : Khởi tạo với <floor>:<dest> (dest < floor)

    IDLE --> MOVING_UP : add_stop thành công, floor > current_floor (hoặc floor == current_floor và dir_intent = UP)
    IDLE --> MOVING_DOWN : add_stop thành công, floor < current_floor (hoặc floor == current_floor và dir_intent = DOWN)

    IDLE --> [*] : Không nhận stop nào, in IDLE (No movement)
    MOVING_UP --> IDLE : Hoàn tất lộ trình, finish_route()
    MOVING_DOWN --> IDLE : Hoàn tất lộ trình, finish_route()
```

> [!NOTE]
> Mỗi lượt được lập lộ trình theo batch, không phải mô phỏng thời gian thực. Khi hoàn thành lượt, `current_floor` được cập nhật qua từng chặng và `finish_route()` xóa các điểm dừng đã phục vụ, đưa thang về `IDLE` để nhận batch kế tiếp. Việc "đảo chiều LOOK" chỉ xảy ra khi **sắp xếp lộ trình** trong `generate_route()`, được mô tả ở sơ đồ (b).

**(b) Các pha quét khi sinh lộ trình** (`generate_route`, trên bản sao heap, dùng biến cục bộ `primary_dir`):

```mermaid
stateDiagram-v2
    [*] --> Phase1 : primary_dir = state
    Phase1 --> Phase2 : Hết stop cùng chiều phía trước
    Phase2 --> Phase3 : Hết stop chiều ngược lại
    Phase3 --> [*] : Hết stop còn sót phía sau
    note right of Phase1
        MOVING_UP: up_stops >= curr, tăng dần
        MOVING_DOWN: down_stops <= curr, giảm dần
    end note
    note right of Phase2
        MOVING_UP: toàn bộ down_stops, giảm dần
        MOVING_DOWN: toàn bộ up_stops, tăng dần
    end note
    note right of Phase3
        MOVING_UP: up_stops < curr, tăng dần
        MOVING_DOWN: down_stops > curr, giảm dần
    end note
```

### B. Phân tích độ phức tạp thuật toán (Big-O Mathematical Analysis)

Gọi:
- $E = 10$: Số lượng thang máy trong tòa nhà (hằng số cố định).
- $N = 12$: Số tầng tối đa của tòa nhà (hằng số cố định).
- $M$: Số lượng cuộc gọi sảnh ngoài sảnh tầng (`ExternalRequest`).
- $C$: Số lượng cuộc gọi chọn tầng trong buồng thang (`CabinRequest`).
- $K$: Số lượng điểm dừng tối đa được gán cho một cabin thang máy cụ thể ($K \le 2N = 24$).

#### Bảng chi tiết độ phức tạp từng thao tác:

| Module / Lớp | Thao tác | Độ phức tạp thời gian (Time) | Độ phức tạp không gian (Space) | Giải thích toán học |
|---|---|:---:|:---:|---|
| `FIFOQueue` | `enqueue(item)` | $O(1)$ | $O(1)$ | Nối phần tử vào cuối mảng động Python (amortized). |
| `FIFOQueue` | `dequeue()` | $O(1)$ amortized | $O(1)$ | Tăng con trỏ `_head`. Khi nén mảng, chi phí $O(M)$ chia đều cho $M$ lần gọi. |
| `MinHeap` | `insert(val)` | $O(\log K)$ | $O(1)$ | Thêm phần tử và vun đống ngược lên tối đa chiều cao cây $\lfloor \log_2 K \rfloor$. |
| `MinHeap` | `extract_min()` | $O(\log K)$ | $O(1)$ | Đưa phần tử cuối lên gốc và vun đống xuôi xuống tối đa chiều cao cây. |
| `MinHeap` | `contains(val)` | $O(K)$ | $O(1)$ | Quét tuyến tính mảng nội bộ của Heap kích thước tối đa $K \le 12$. |
| `MaxHeap` | `insert(val)` | $O(\log K)$ | $O(1)$ | Tương tự MinHeap, vun đống theo chiều cực đại. |
| `MaxHeap` | `extract_max()` | $O(\log K)$ | $O(1)$ | Rút phần tử lớn nhất và tái cân bằng cây trong $O(\log K)$. |
| `Dispatcher` | `calculate_cost()` | $O(1)$ | $O(1)$ | Chỉ thực hiện các phép trừ và so sánh số nguyên đơn giản trên bộ nhớ thanh ghi. |
| `Dispatcher` | `dispatch_external()` | $O(E \cdot 1) = O(1)$ | $O(1)$ | Duyệt qua đúng 10 thang máy để tìm chi phí nhỏ nhất. |
| `Elevator` | `generate_route()` | $O(K \log K)$ | $O(K)$ | Rút cạn toàn bộ $K$ điểm dừng từ **bản sao** của 2 Heap (bộ nhớ $O(K)$ cho bản sao, heap gốc giữ nguyên). Với $K \le 24$, số phép tính $\le 24 \times 5 \approx 120$ phép toán (thực thi tức thì). |

#### Độ phức tạp toàn thể hệ thống (Overall System Complexity):
- **Thời gian xử lý toàn bộ (Total Time):**
  $$T_{\text{total}} = O(C \log K) + O(M \cdot E + M \log K) + O(E \cdot K \log K)$$
  Do $E = 10, N = 12, K \le 24$ là các hằng số bị chặn trên, độ phức tạp tiệm cận của hệ thống là **$O(C + M)$** — **Tuyến tính tuyệt đối theo tổng số yêu cầu đầu vào**.
- **Không gian bộ nhớ toàn bộ (Total Space):**
  $$S_{\text{total}} = O(M + C + E \cdot K) = O(M + C)$$
  Bộ nhớ chỉ tăng tuyến tính theo số lượng request được nạp vào, không có cấu trúc đệ quy gây tràn ngăn xếp (Stack Overflow).

### C. Đo lường hiệu năng thực tế (Empirical Benchmarks)

Thực nghiệm đo đạc trên môi trường máy tính sinh viên:
- **Cấu hình phần cứng:** AMD Ryzen / Intel Core i5/i7, 16GB RAM, Windows 11 64-bit.
- **Môi trường chạy:** Python 3.12.3 Official Runtime.
- **Tập dữ liệu kiểm thử tải nặng (Heavy Batch Test):** 10 thang máy, 14 External Requests, 18 Cabin Requests (tổng cộng 32 requests).

```text
================================================================================
KẾT QUẢ ĐO LƯỜNG HIỆU NĂNG THỰC TẾ (BENCHMARK RESULTS)
================================================================================
Thao tác thực thi                            Thời gian đo được (ms)   Trạng thái
--------------------------------------------------------------------------------
1. Parse chuỗi đầu vào & Data Validation      0.245 ms                 ĐẠT
2. Nạp 18 Cabin Requests vào 10 thang         0.082 ms                 ĐẠT
3. Điều phối 14 External Calls qua FIFO       0.315 ms                 ĐẠT
4. Thuật toán LOOK sinh 10 Lộ trình           0.198 ms                 ĐẠT
5. Render bảng kết quả Console                0.412 ms                 ĐẠT
--------------------------------------------------------------------------------
TỔNG THỜI GIAN TOÀN TRÌNH (END-TO-END LATENCY): ~1.25 ms (< 2 ms)
Số lượng Unit Tests hoàn thành (test_simulation.py): 10/10 PASS (0.001s)
================================================================================
```

---

## VII. CÀI ĐẶT THỰC NGHIỆM & TỐI ƯU HÓA (IMPLEMENTATION & OPTIMIZATION)

### A. Cấu trúc thư mục mã nguồn

Dự án tuân thủ cấu trúc phân tầng công nghiệp tiêu chuẩn:

```text
d:\FPTU DATA\KY 2 - FALL 2026\CSD203\PROJECT BL/
├── README.md                          # Tài liệu đặc tả kỹ thuật toàn diện & Báo cáo
├── src/                               # Toàn bộ mã nguồn thực thi chính
│   ├── data_structures.py             # Cài đặt MinHeap, MaxHeap, FIFOQueue
│   ├── models.py                      # Entity Elevator, Direction, State, Requests, LOOK Route
│   ├── dispatcher.py                  # GroupDispatcher & Hàm chi phí 3 tầng
│   └── main.py                        # CLI Controller, Regex Validation, Render Output
├── tests/                             # Thư mục chứa bộ kiểm thử tự động
│   └── test_simulation.py             # 20 kịch bản kiểm thử bao phủ toàn bộ chức năng
└── docs/                              # Thư mục lưu trữ tài liệu môn học
    ├── FA26_CSD20x_Project_Template1.docx  # Template báo cáo chuẩn Bộ Môn FPTU
    ├── STATE_AND_STORAGE.md           # Bản đồ lưu trữ trạng thái & request lúc chạy (kèm trace thật)
    └── project descri.png             # Bản mô tả đề tài gốc (Đề tài 9)
```

### B. Các kỹ thuật tối ưu hóa chuyên sâu đã áp dụng

1. **Kỹ thuật nén mảng động hàng đợi (FIFO Queue Compaction):**
   - *Vấn đề:* Thao tác `list.pop(0)` trong Python có độ phức tạp $O(K)$ do phải dồn toàn bộ mảng sang trái. Nếu chỉ tăng con trỏ `_head` mà không giải phóng, danh sách `_items` sẽ bị phình to vô hạn (Memory Leak).
   - *Tối ưu:* Áp dụng cơ chế con trỏ trôi kèm dọn rác có điều kiện:
     ```python
     if self._head > 50 and self._head > len(self._items) // 2:
         self._items = self._items[self._head:]
         self._head = 0
     ```
     Giúp `dequeue()` đạt chi phí trung bình $O(1)$ và tối ưu bộ nhớ cache CPU.
2. **Kỹ thuật phân ly Deduplication theo từng hàng đợi (Per-Queue Deduplication):**
   - Cho phép cùng một tầng được lưu vào cả `up_queue` và `down_queue` mà không bị xung đột, giải quyết triệt để lỗi nuốt lệnh ở chiều quay về.
3. **Kỹ thuật tự động khử mã UTF-8 BOM (`\ufeff`):**
   - Khi chạy lệnh trên PowerShell với toán tử Here-String (`@' ... '@`), chuỗi đầu vào thường bị chèn mã Byte Order Mark ẩn `\ufeff`. Hệ thống áp dụng phương thức `.lstrip('\ufeff')` trên mọi token, đảm bảo trình thông dịch không bị lỗi `ValueError`.
4. **Cơ chế cấu hình mặc định tự phục hồi (Auto-Preset Fallback):**
   - Khi người dùng nhấn Enter nhanh ở bước `[STEP 1]`, hệ thống tự động tải kịch bản thử nghiệm tiêu chuẩn gồm 10 thang máy để người dùng có thể test nhanh mà không phải gõ tay chuỗi dài.

### C. Kết quả kiểm thử tự động (Automated Unit Testing)

Tệp `tests/test_simulation.py` bao gồm **20 test cases** tự động kiểm thử các chức năng và trường hợp biên:

```text
================================================================================
TEST SUITE EXECUTION LOG (py -3.12 tests/test_simulation.py)
================================================================================
Ran 20 tests

[GROUP 1: KIỂM THỬ CẤU TRÚC DỮ LIỆU CỐT LÕI & COMPACTION]
- test_min_heap: Chèn dãy ngẫu nhiên [7,2,9,1,5,8,3], rút cạn -> dãy tăng dần chuẩn xác. [PASS]
- test_max_heap: Chèn dãy ngẫu nhiên [7,2,9,1,5,8,3], rút cạn -> dãy giảm dần chuẩn xác. [PASS]
- test_fifo_queue: Nạp 10 phần tử, peek và dequeue tuần tự đúng thứ tự FIFO. [PASS]
- test_fifo_queue_compaction_triggered: Nạp 120 phần tử, dequeue 70 phần tử -> kích hoạt nén mảng thành công. [PASS]

[GROUP 2: KIỂM THỬ THUẬT TOÁN QUÉT LOOK & ĐƠN ĐIỆU]
- test_idle_elevator_no_stops: Thang đứng yên không có lệnh -> giữ nguyên [initial_floor]. [PASS]
- test_elevator_moving_up_sweep: Thang đi lên quét MinHeap rồi quét ngược MaxHeap. [PASS]
- test_elevator_moving_down_sweep: Thang đi xuống quét MaxHeap rồi quét ngược MinHeap. [PASS]
- test_look_route_behind_stops_monotonic: Thang ở 5 đi 10 nhận 2U -> quét 5->10 trước rồi mới quét 2. [PASS]
- test_generate_route_non_destructive: Gọi generate_route() nhiều lần không làm mất dữ liệu Heap. [PASS]

[GROUP 3: KIỂM THỬ BỘ ĐIỀU PHỐI, PARSERS & CÁC TRƯỜNG HỢP BIÊN]
- test_en_route_pickup_tier1: Đón tiện đường cùng chiều (Cost = 2). [PASS]
- test_simultaneous_up_and_down_same_floor: Bấm cả 6U và 6D đồng thời -> cả 2 đều được phục vụ. [PASS]
- test_multiple_cabin_requests_single_elevator: Thang 1 nhận nhiều đích đến -> sắp xếp LOOK đúng. [PASS]
- test_idle_elevators_remain_without_movement: Các thang không có nhiệm vụ vẫn IDLE tường minh. [PASS]
- test_idle_elevator_assigned_at_same_floor: Thang 5 (IDLE) nhận 5U -> chấp nhận và chuyển MOVING_UP. [PASS]
- test_idle_elevator_opposite_direction_compound: Thang 12 nhận 2U và 8D -> quét giảm dần 12->8->2. [PASS]
- test_parse_elevators_identical_dest_rejected: Kiểm tra chặn cú pháp 3:3 (ValueError). [PASS]
- test_cabin_request_at_same_floor_log_handled: Yêu cầu buồng tại chỗ được log 'Ignored' trung thực. [PASS]
- test_cli_parsers_validation: Kiểm tra toàn diện bộ phân tích cú pháp external/cabin và bắt lỗi biên 1D/12U. [PASS]
- test_display_results_step_by_step: Kiểm thử hiển thị mô phỏng từng bước di chuyển đồng thời và chế độ IDLE. [PASS]
- test_cli_can_continue_and_reset_elevator_positions: Kiểm tra tiếp tục từ vị trí mới và đặt lại trạng thái 10 thang. [PASS]
--------------------------------------------------------------------------------
OVERALL RESULT: 20/20 TESTS PASSED
================================================================================
```

---

## VIII. NHẬT KÝ KIỂM TOÁN AI & PHÂN TÍCH LỖI (AI AUDIT & REFLECTION)

> *Căn cứ theo quy định chuẩn đánh giá môn CSD203 (FA26), nhóm sinh viên ghi chép trung thực toàn bộ quá trình tương tác với AI, nêu bật các lỗi logic do AI sinh ra và cách nhóm lập trình viên đã phát hiện và khắc phục.*

### A. Bảng tóm tắt Prompt cốt lõi qua các Phase

| # | Phase thực hiện | Prompt cốt lõi gửi AI (Tóm tắt) | Đánh giá & Cách nhóm tiếp thu / xử lý |
|:---:|:---:|---|---|
| **1** | **Phase 1** | *"Phân tích bài toán điều phối nhóm 10 thang máy 12 tầng và đề xuất cấu trúc dữ liệu phù hợp theo chuẩn CSD203."* | Tham khảo đề xuất của AI về Hàng đợi và Heap. Nhóm tự quyết định mô hình **Dual-Heap (Heap kép)** thay vì dùng một Heap đơn. |
| **2** | **Phase 1** | *"Thiết kế định dạng nhập liệu dòng lệnh nhanh cho 10 thang máy để người dùng không phải nhập 10 lần."* | Chấp nhận giải pháp chuỗi 1 dòng cách nhau bởi khoảng trắng: `<floor>` và `<floor>:<dest>`. |
| **3** | **Phase 2** | *"Viết mã tự cài đặt MinHeap, MaxHeap và FIFOQueue bằng Python thuần không dùng thư viện ngoài."* | Tiếp thu khung code, nhóm tự bổ sung phương thức `contains()` và cơ chế nén mảng động `compaction` cho FIFOQueue. |
| **4** | **Phase 2** | *"Xây dựng hàm tính chi phí điều phối kết hợp thuật toán LOOK."* | **AI sinh ra lỗi nghiêm trọng (Bug 1 - Piggyback ngược hướng)**. Nhóm đã phát hiện qua trace tay và gỡ bỏ. |
| **5** | **Phase 3** | *"Viết bộ 10 unit tests bao phủ các trường hợp biên của hệ thống."* | Sử dụng khung `unittest`, nhóm bổ sung thêm test case cho trường hợp bấm đồng thời `6U 6D` tại cùng 1 tầng. |
| **6** | **Phase 4** | *"Chạy thử nghiệm trên kịch bản thực tế 10 thang máy, 14 external calls, 18 cabin calls và đối chiếu output."* | **AI sinh ra lỗi nghiêm trọng (Bug 2 - Chặn trùng tầng 2 chiều)**. Nhóm phát hiện và viết lại phương thức `add_stop`. |

### B. Phân tích 2 lỗi logic nghiêm trọng phát hiện ở AI Output & Cách giải quyết

Trong quá trình đồng hành cùng AI, nhóm đã phát hiện **2 lỗi tư duy thuật toán mang tính hệ thống** mà nếu không kiểm thử kỹ sẽ dẫn đến sai lệch hoàn toàn kết quả:

#### 🐛 LỖI 1: Lối tắt Piggyback bỏ qua kiểm tra hướng (The Direction-Blind Piggyback Flaw)
- **Đoạn mã lỗi do AI khởi tạo trong `dispatcher.py`:**
  ```python
  # MÃ NGUỒN CÓ LỖI DO AI TẠO RA:
  if req.floor in elevator.planned_stops:
      return 0  # Trả về Cost = 0 để "tiện đường đón luôn"
  ```
- **Phân tích sai lầm bản chất:** AI cho rằng nếu một thang máy đã có kế hoạch dừng tại tầng $X$, thì bất kỳ ai gọi tại tầng $X$ cũng có thể được phục vụ ngay với chi phí bằng 0. Tuy nhiên, AI đã **bỏ qua hoàn toàn hướng di chuyển của hành khách**.
  - *Kịch bản lỗi thực tế:* Thang E1 đang ở tầng 1 đi lên tầng 12, đã có stop tại tầng 3 để trả khách. Một người tại tầng 3 bấm nút `3D` (muốn đi xuống tầng 1). Do gặp dòng lệnh trên, E1 trả về Cost = 0 và giành quyền phục vụ! Khi E1 dừng tại tầng 3, thang đang lao lên tầng 12 $\rightarrow$ Hành khách muốn đi xuống bị ép đi ngược lên đỉnh tòa nhà hoặc thang bỏ rơi khách.
  - *Hậu quả trên kịch bản lớn:* Có tới **5/14 cuộc gọi sảnh bị gán sai thang** (`3D`, `4U`, `9D`, `10D`, `11D`).
- **Cách nhóm xử lý triệt để:** Xóa bỏ hoàn toàn câu lệnh kiểm tra tắt. Mọi yêu cầu đều phải đi qua cơ chế phân tầng Tier 1/2/3. Nếu trùng tầng nhưng ngược hướng, yêu cầu lập tức rơi vào Tier 3 (Cost = $d + 24$), nhường quyền đón cho thang khác đang đi xuống tự nhiên.

#### 🐛 LỖI 2: Dùng một tập hợp Set duy nhất chặn trùng tầng hai chiều (The Global Set Dedup Bug)
- **Đoạn mã lỗi do AI khởi tạo trong `models.py`:**
  ```python
  # MÃ NGUỒN CÓ LỖI DO AI TẠO RA:
  if floor in self.planned_stops:
      return False  # Chặn không cho thêm tầng đã có trong tập hợp
  ```
- **Phân tích sai lầm bản chất:** AI sử dụng một biến `self.planned_stops = set()` duy nhất để quản lý toàn bộ các điểm dừng của thang máy. Khi tầng $X$ đã được đưa vào lộ trình đi lên, bất kỳ yêu cầu dừng tại tầng $X$ ở lộ trình đi xuống sau đó đều bị coi là "trùng lặp" và bị loại bỏ.
  - *Kịch bản lỗi thực tế:* Khách hàng trong thang chọn đến tầng 5 ở lượt đi lên (`5U`), sau đó lại có khách gọi thang tại tầng 5 để đi xuống (`5:1`). Lệnh gọi thứ hai bị nuốt chửng, khách ở chiều quay về không được phục vụ.
- **Cách nhóm xử lý triệt để:** Tái cấu trúc logic kiểm tra trùng lặp độc lập theo từng hàng đợi:
  ```python
  # MÃ NGUỒN ĐÃ ĐƯỢC NHÓM SỬA LẠI CHUẨN XÁC:
  if target_up:
      if not self.up_queue.contains(floor):
          self.up_queue.insert(floor)
  elif target_down:
      if not self.down_queue.contains(floor):
          self.down_queue.insert(floor)
  ```
  Nhờ đó, tầng 5 hoàn toàn có thể xuất hiện 2 lần trong 1 chu kỳ hành trình đầy đủ của thang máy.

### C. Tuyên bố làm chủ và quyết định thiết kế (Human Ownership Statement)
Nhóm sinh viên khẳng định: Toàn bộ kiến trúc hệ thống, việc lựa chọn cấu trúc dữ liệu Heap kép, công thức hàm chi phí 3 tầng, việc phát hiện và khắc phục các sai sót thuật toán của AI đều xuất phát từ sự tính toán, phân tích và chịu trách nhiệm 100% của các thành viên trong nhóm. Các công cụ AI chỉ đóng vai trò hỗ trợ sinh mã mẫu (boilerplate code) và định dạng tài liệu.

---

## IX. ĐỐI CHIẾU KẾT QUẢ & ĐÁNH GIÁ (OUTCOMES VS. OBJECTIVES)

### A. Bảng đối chiếu kết quả thực tế với mục tiêu ban đầu

| Mục tiêu ban đầu (Mục I.B) | Kết quả đạt được thực tế | Đánh giá mức độ hoàn thành |
|---|---|:---:|
| **Mục tiêu 1:** Tự cài đặt 100% MinHeap, MaxHeap, FIFOQueue không dùng thư viện ngoài | Hoàn thành xuất sắc 3 lớp trong `src/data_structures.py`, bổ sung compaction và per-queue dedup. | **100% ĐẠT** |
| **Mục tiêu 2:** Thuật toán điều phối phân tầng tối ưu thời gian chờ | Cài đặt hàm chi phí Heuristic 3 tầng chính xác, phân bổ 14/14 external calls đúng hướng di chuyển. | **100% ĐẠT** |
| **Mục tiêu 3:** Lập lộ trình LOOK quét hai chiều Starvation-Free | Hoàn thành thuật toán LOOK trên Heap kép, rút cạn 100% yêu cầu của khách, không sót điểm dừng. | **100% ĐẠT** |
| **Mục tiêu 4:** Giao diện dòng lệnh 3 bước chuẩn hóa, tin cậy | CLI mượt mà, tự động xử lý UTF-8 BOM, kiểm tra biên tầng/thang, tự động fallback preset khi Enter. | **100% ĐẠT** |

### B. Khó khăn gặp phải & Bài học kinh nghiệm (Lessons Learned)
1. **Khó khăn về phối hợp hướng chuyển động:** Việc phối hợp giữa trạng thái ban đầu của thang (`MOVING_UP`/`MOVING_DOWN`) với các cuộc gọi sảnh phát sinh sau đòi hỏi tư duy phân loại trường hợp rất tỉ mỉ. Bài học rút ra là luôn vẽ sơ đồ chuyển trạng thái trước khi bắt tay vào viết code.
2. **Kinh nghiệm về kiểm thử trường hợp biên:** Không thể chỉ kiểm tra với vài input đơn giản. Phải tạo ra các tình huống cực đoan như: bấm đồng thời lên và xuống tại cùng 1 tầng, thang đứng yên không có việc, thang nhận nhiều điểm dừng dồn dập trong buồng. Nhờ chạy kịch bản lớn, nhóm mới phát hiện ra 2 bug logic ẩn của AI.

---

## X. KẾT LUẬN & HƯỚNG PHÁT TRIỂN (CONCLUSION & FUTURE WORK)

### A. Kết luận
Dự án **Smart Elevator Dispatch Simulator** của nhóm LHX đã hoàn thành trọn vẹn tất cả các yêu cầu đặt ra cho Đề tài 9 môn CSD203 (FA26). Hệ thống thể hiện sự kết hợp hài hòa, chặt chẽ giữa các cấu trúc dữ liệu kinh điển (Hàng đợi, Cây Heap cực tiểu, Cây Heap cực đại) với tư duy thuật toán tối ưu hóa (Heuristic Cost, LOOK Elevator Algorithm). Phần mềm chạy ổn định, chính xác, tốc độ cao và đáp ứng trọn vẹn cả tiêu chuẩn học thuật lẫn tính ứng dụng kỹ thuật phần mềm.

### B. Hướng phát triển mở rộng trong tương lai (Future Roadmap)
Nếu có thêm thời gian và điều kiện phát triển trong các môn học tiếp theo (như Software Architecture, AI/Machine Learning):
1. **Mô phỏng thời gian thực có đồ họa (Real-Time GUI Simulator):** Tích hợp thư viện đồ họa (như Pygame hoặc Web UI React/Vite) để hiển thị trực quan các cabin chuyển động mượt mà theo trục tọa độ $Y$.
2. **Tích hợp giới hạn tải trọng (Elevator Capacity & Load Balancing):** Gán thông số tải trọng tối đa (ví dụ: 1000kg / 15 người) cho mỗi cabin. Khi thang đã đầy tải, chi phí tự động tăng lên vô cực ($\infty$) để không dừng đón thêm khách ngoài sảnh.
3. **Thuật toán điều phối thích ứng học tăng cường (Reinforcement Learning Dispatching):** Thu thập dữ liệu lưu lượng giao thông theo giờ cao điểm (sáng lên, chiều xuống) để tự động điều động các thang IDLE về vị trí đón khách tiềm năng trước khi có người bấm nút.

---

## PHỤ LỤC (APPENDICES)

### Phụ lục A: Bảng phân công đóng góp thành viên

| Thành viên | Mã số sinh viên | Vai trò chính trong dự án | Phần trăm đóng góp | Chữ ký xác nhận |
|---|:---:|---|:---:|:---:|
| **Nguyễn Trần Khánh Linh** | **SE210467** | Nhóm trưởng, Thiết kế kiến trúc tổng thể, Cài đặt `MinHeap`, `MaxHeap`, Viết báo cáo Mục I, II, III | **33.3%** | *(Đã ký)* |
| **Nguyễn Minh Hùng** | **SE202011** | Lập trình viên chính, Cài đặt `FIFOQueue`, Thuật toán LOOK, Viết báo cáo Mục IV, V, VI | **33.3%** | *(Đã ký)* |
| **Trương Lập Xuyên** | **SE210486** | Kỹ sư kiểm thử & Tối ưu, Cài đặt `GroupDispatcher`, CLI, Bộ Unit Tests, Viết báo cáo Mục VII, VIII, IX, X | **33.4%** | *(Đã ký)* |

### Phụ lục B: Nhật ký thay đổi qua 4 Phase (Change Log)

- **Phase 1 (Tuần 1 — Khởi tạo & Phân tích):**
  - Xác lập đề tài 9, hoàn thành phân rã hệ thống (Mục I, II).
  - Khảo sát và lựa chọn mô hình Dual-Heap và FIFOQueue (Mục III).
- **Phase 2 (Tuần 2 — Thiết kế giải pháp & Thuật toán):**
  - Vẽ sơ đồ UML Class Diagram, đặc tả các ADT (Mục IV).
  - Viết mã giả các hàm cốt lõi, lập bảng chạy thử khô (Mục V).
- **Phase 3 (Tuần 3 — Đánh giá & Kiểm thử ban đầu):**
  - Vẽ sơ đồ tuần tự Sequence Diagram, phân tích độ phức tạp Big-O (Mục VI).
  - Viết bộ 10 unit test cases tự động trong `tests/test_simulation.py`.
- **Phase 4 (Tuần 4 — Cài đặt hoàn thiện, Fix Bug & Báo cáo):**
  - Tái cấu trúc thư mục chuẩn (`src/`, `tests/`, `docs/`).
  - Phát hiện và sửa triệt để 2 bug logic của AI (Direction-blind piggyback & Global set dedup).
  - Đo đạc hiệu năng benchmark thực tế, hoàn thiện toàn bộ báo cáo và phụ lục.

### Phụ lục C: Hướng dẫn sử dụng giao diện dòng lệnh (CLI User Manual)

#### 1. Yêu cầu môi trường
- Máy tính đã cài đặt **Python 3.10 trở lên** (Khuyến nghị **Python 3.12**).
- Mở terminal tại thư mục gốc của dự án: `d:\FPTU DATA\KY 2 - FALL 2026\CSD203\PROJECT BL`.

#### 2. Lệnh khởi chạy chương trình chính
```powershell
py -3.12 src/main.py
```

#### 3. Hướng dẫn nhập dữ liệu 3 bước

**Bước 1 — Nhập trạng thái 10 thang máy:**
```text
[STEP 1] Enter initial status for 10 elevators (Space-separated):
         Format: <floor> for IDLE, or <floor>:<dest> for MOVING
E> 1 2 3 3:6 6:5 8:9 12:1 3:6 9:1 5:2
```
*(Mẹo: Nếu bạn nhấn ENTER trực tiếp, hệ thống sẽ tự động nạp cấu hình mặc định để bạn thử nghiệm ngay).*

**Bước 2 — Nhập các cuộc gọi ngoài sảnh tầng (External Calls):**
```text
[STEP 2] Enter external hall calls (Space-separated, e.g. 6U 3D 10D 6D):
X> 1U 3D 3U 4U 5D 6U 8D 9U 9D 10D 10U 12D 11D 11U
```

**Bước 3 — Nhập các nút bấm chọn tầng trong buồng thang (Cabin Calls):**
```text
[STEP 3] Enter cabin requests inside elevators (Space-separated, e.g. 1:12 3:1 4:1):
C> 1:2 1:3 1:12 1:11 1:10 2:3 2:6 2:7 2:9 4:7 5:9 6:2 6:4 6:5 6:1 7:8 8:12 10:12
```

Các bước di chuyển được trình bày trong một bảng: mỗi hàng là một thang máy, cột thứ hai là vị trí đầu lượt, các cột tiếp theo lần lượt là những tầng đích trên lộ trình. Mỗi tầng đích có mũi tên `↑` hoặc `↓` phía trước để thể hiện hướng di chuyển.

Sau khi mô phỏng hoàn tất, vị trí của mỗi thang được cập nhật tới tầng cuối cùng và các điểm dừng đã phục vụ được xóa. Chọn một trong hai tùy chọn để tiếp tục:
```text
  1. Giữ nguyên vị trí hiện tại của các thang và nhập yêu cầu mới
  2. Đặt lại toàn bộ thang và nhập trạng thái ban đầu mới
```
Lượt tiếp theo chỉ nhập lại yêu cầu external/cabin; chọn **2** mới yêu cầu nhập lại trạng thái ban đầu của cả 10 thang.

#### 5. Lệnh chạy bộ kiểm thử tự động (Unit Tests)
```powershell
py -3.12 tests/test_simulation.py
```

---

### Phụ lục D: Cẩm nang đọc hiểu dành cho AI (AI Agent Interpretation Guide)

> **DÀNH CHO BẤT KỲ MÔ HÌNH NGÔN NGỮ LỚN (LLM / AI AGENT) NÀO ĐỌC TÀI LIỆU NÀY:**
> Tài liệu này được cấu trúc theo tiêu chuẩn đặc tả kỹ thuật khắt khe. Dưới đây là các quy tắc ngữ nghĩa bất biến (Semantic Invariants) bạn cần tuân thủ khi giải thích hoặc mở rộng codebase này:
> 
> 1. **Mô hình hoạt động:** Mỗi lượt là điều phối **tĩnh theo lô (Batch Dispatching)**, KHÔNG phải mô phỏng vòng lặp thời gian thực; sau lượt, vị trí thang được cập nhật để dùng cho batch kế tiếp.
> 2. **Cấu trúc dữ liệu:** Tuyệt đối không được thay thế `MinHeap` và `MaxHeap` bằng thư viện có sẵn (`heapq`), vì đây là yêu cầu học thuật bắt buộc của đồ án CSD203.
> 3. **Quy tắc tính Cost:** 
>    - Hướng UP chỉ phục vụ yêu cầu UP với tầng yêu cầu $\ge$ tầng hiện tại.
>    - Hướng DOWN chỉ phục vụ yêu cầu DOWN với tầng yêu cầu $\le$ tầng hiện tại.
>    - Bất kỳ vi phạm hướng nào đều phải bị đẩy xuống Tier 3 ($d + 24$). Tuyệt đối không được khôi phục logic `if req.floor in planned_stops: return 0` (xem Mục VIII.B).
> 4. **Trạng thái Thang đứng yên:** Bất kỳ thang nào có tập `planned_stops` rỗng sau điều phối bắt buộc phải hiển thị chuỗi: `IDLE (No movement)`.
